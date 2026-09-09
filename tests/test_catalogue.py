"""Validate source loading, migration integrity and generated-page navigation."""
import copy
import importlib.util
import json
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlparse
import yaml

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('build',ROOT/'scripts/build.py')
build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        for key in ['href','src']:
            if key in attrs:self.links.append(attrs[key])
        if 'id' in attrs:self.ids.append(attrs['id'])

class CatalogueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.data=build.load_problems();cls.outputs=build.generate()
    def test_all_internal_links(self):
        for name,content in self.outputs.items():
            if not name.endswith('.html'):continue
            parser=Links();parser.feed(content)
            self.assertEqual(len(parser.ids),len(set(parser.ids)),name)
            for link in parser.links:
                parsed=urlparse(link)
                if parsed.scheme:continue
                target=(ROOT/name).parent/unquote(parsed.path) if parsed.path else ROOT/name
                self.assertTrue(target.exists(),f'{name} -> {link}')
                if parsed.fragment:
                    dest=Links();dest.feed(target.read_text());self.assertIn(parsed.fragment,dest.ids)
    def test_source_links_preserved(self):
        original=(ROOT/'archive/original-notes.md').read_text().split('<!--')[0]
        active=json.dumps(self.data)+''.join(self.outputs.values())+(ROOT/'docs/resources.md').read_text()+(ROOT/'docs/visualizations.md').read_text()
        for _,url in build.LINK.findall(original):
            if url in ['https://awesome.re','https://awesome.re/badge.svg']:continue
            self.assertIn(url,active,url)
    def test_outputs_current(self):
        for name,content in self.outputs.items():self.assertEqual((ROOT/name).read_text(),content,name)
    def test_yaml_multiple_files_and_normalization(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp);(folder/'nested').mkdir()
            a=copy.deepcopy(self.data[0]);b=copy.deepcopy(self.data[1]);a['events'][0]['year']=2026
            (folder/'one.yaml').write_text(yaml.safe_dump({'contributor':'tester','problems':[a]}))
            (folder/'nested/two.yml').write_text(yaml.safe_dump({'problems':[b]}))
            loaded=build.load_problems(folder)
            self.assertEqual({p['id'] for p in loaded},{a['id'],b['id']})
            self.assertIsInstance(next(p for p in loaded if p['id']==a['id'])['events'][0]['year'],str)
    def test_event_dates_and_sort_keys(self):
        event=copy.deepcopy(self.data[0]['events'][0]);event['year']='2026';event['date']='2026-07'
        problem=copy.deepcopy(self.data[0]);problem['events']=[event]
        build.validate([problem])
        self.assertEqual(build.format_date(event['date']),'Jul 2026')
        self.assertEqual(build.problem_date_key(problem),'2026-07-00')
        event['date']='2025-12'
        with self.assertRaisesRegex(ValueError,'within its year'):build.validate([problem])
    def test_duplicate_ids_name_both_files(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)
            for name in ['one.yaml','two.yaml']:(folder/name).write_text(yaml.safe_dump({'problems':[self.data[0]]}))
            with self.assertRaisesRegex(ValueError,r'two.yaml.*one.yaml'):build.load_problems(folder)
    def test_duplicate_keys_and_unsafe_yaml(self):
        for content in ['problems: []\nproblems: []\n','problems: !!python/object/apply:os.system [echo unsafe]']:
            with tempfile.TemporaryDirectory() as temp:
                (Path(temp)/'bad.yaml').write_text(content)
                with self.assertRaises(ValueError):build.load_problems(temp)
    def test_unknown_fields_categories_and_urls(self):
        for mutate in [lambda p:p.update(category='Incidents'),lambda p:p.update(category='Collections'),lambda p:p.update(typo='x'),lambda p:p['events'][0]['links'][0].update(url='javascript:alert(1)')]:
            p=copy.deepcopy(self.data[0]);mutate(p)
            with self.assertRaises(ValueError):build.validate([p])
    def test_text_is_escaped(self):
        self.assertNotIn('<script>',build.rich('<script>alert(1)</script>'))
    def test_models_and_scoped_badges(self):
        for p in self.data:
            self.assertTrue(build.models(p))
            self.assertIn('class="badges"',build.problem_badges(p))
        audit=next(p for p in self.data if p['id']=='minif2f-audit')
        self.assertIn('verified (audit)',build.problem_badges(audit))
    def test_no_active_slogans_or_old_pages(self):
        for text in [*self.outputs.values(),json.dumps(self.data)]:
            for phrase in ['A living catalogue','A proof has a scope','Lesson:','Reading the evidence','The good, the bad, and the QED']:
                self.assertNotIn(phrase,text)
        for path in ['data/problems.json','data/resources.json','docs-site/guide.html','docs-site/resources.html']:
            self.assertFalse((ROOT/path).exists(),path)
    def test_source_collections_are_split(self):
        ids={p['id'] for p in self.data}
        self.assertFalse(ids & {'kourovka','ten-proofs','banach-collection','erdos-oeis-sweep','aletheia-erdos','erdos-novelty'})
        self.assertEqual(sum(p['id'].startswith('kourovka-') for p in self.data),9)
        self.assertTrue({'erdos-1196','erdos-1217','erdos-164','erdos-333'} <= ids)
    def test_chart_counting_deduplicates(self):
        records=[{'models':['A','A','B']},{'models':['A']}]
        self.assertEqual(build.counts(records,'models'),[('A',2),('B',1)])

if __name__=='__main__':unittest.main()
