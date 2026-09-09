#!/usr/bin/env python3
"""Load contributor YAML files and generate the README and static website."""

import argparse
from collections import Counter
from datetime import date
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse
import yaml

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ["Research", "Competitions", "Historical"]
LABELS = dict(zip(CATEGORIES, ["Research problems", "Competition problems", "Historical results"]))
EVIDENCE = ["verified", "machine-checked", "self-reported", "disputed", "debunked"]
REPO = "https://github.com/subroy13/awesome-ai-proofs"
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^\s]+?)\)")


class UniqueSafeLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys rather than silently overwriting data."""

    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str):
                raise ValueError("YAML mapping keys must be strings")
            if key in result:
                raise ValueError(f"Duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def load_problems(folder=None):
    folder = Path(folder) if folder is not None else ROOT / "data/problems"
    paths = sorted(p for p in folder.rglob("*") if p.suffix.lower() in (".yaml", ".yml"))
    if not paths:
        raise ValueError(f"No YAML files found in {folder}")
    items, locations = [], {}
    for path in paths:
        try:
            document = yaml.load(path.read_text(), Loader=UniqueSafeLoader)
            if not isinstance(document, dict) or set(document) - {"problems", "contributor"}:
                raise ValueError("Expected a problems list and optional contributor name")
            if not isinstance(document.get("problems"), list):
                raise ValueError("problems must be a list")
            for problem in document["problems"]:
                if not isinstance(problem, dict):
                    raise ValueError("Each problem must be a mapping")
                identity = problem.get("id")
                if not isinstance(identity, str):
                    raise ValueError("Problem id must be a string")
                if identity in locations:
                    raise ValueError(f"Duplicate problem id {identity!r}; also in {locations[identity]}")
                locations[identity] = path
                for event in problem.get("events", []):
                    if isinstance(event.get("year"), int):
                        event["year"] = str(event["year"])
                    if isinstance(event.get("date"), date):
                        event["date"] = event["date"].isoformat()
                    if isinstance(event.get("reviewed_on"), date):
                        event["reviewed_on"] = event["reviewed_on"].isoformat()
                items.append(problem)
        except (yaml.YAMLError, ValueError, TypeError, AttributeError) as error:
            raise ValueError(f"{path}: {error}") from error
    validate(items)
    return sorted(items, key=lambda p: (CATEGORIES.index(p["category"]), p["title"].casefold(), p["id"]))


def strings(value, label):
    if not isinstance(value, list) or not value or not all(isinstance(v, str) and v.strip() for v in value):
        raise ValueError(f"{label} must be a nonempty list of strings")


def validate(items):
    seen = set()
    for p in items:
        required = {"id", "title", "subjects", "category", "question", "caveat", "events"}
        if set(p) != required:
            raise ValueError(f"Invalid problem fields: {set(p) ^ required}")
        for field in required - {"subjects", "events"}:
            if not isinstance(p[field], str) or not p[field].strip():
                raise ValueError(f"Missing text: {field}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", p["id"]) or p["id"] in seen:
            raise ValueError(f'Invalid or duplicate id: {p["id"]}')
        seen.add(p["id"])
        if p["category"] not in CATEGORIES:
            raise ValueError(f'Unknown category: {p["category"]}')
        strings(p["subjects"], "subjects")
        if not isinstance(p["events"], list) or not p["events"]:
            raise ValueError("events must be a nonempty list")
        for e in p["events"]:
            required_e = {
                "title",
                "year",
                "summary",
                "links",
                "reported_evidence",
                "reviewed_on",
                "review_note",
                "models",
                "evidence_scope",
            }
            if required_e - set(e) or set(e) - required_e - {"date", "source_group"}:
                raise ValueError(f'Invalid event fields in {p["id"]}')
            for field in ["title", "summary", "review_note", "evidence_scope"]:
                if not isinstance(e[field], str) or not e[field].strip():
                    raise ValueError(f"Missing event {field}")
            if not isinstance(e["year"], str) or not re.fullmatch(r"\d{4}(?:-\d{4})?", e["year"]):
                raise ValueError("Year must be YYYY or YYYY-YYYY")
            years = list(map(int, e["year"].split("-")))
            if years != sorted(years):
                raise ValueError("Reversed year range")
            if "date" in e:
                if not isinstance(e["date"], str) or not re.fullmatch(r"\d{4}(?:-\d{2}(?:-\d{2})?)?", e["date"]):
                    raise ValueError("Date must be YYYY, YYYY-MM or YYYY-MM-DD")
                parts = list(map(int, e["date"].split("-")))
                if len(parts) >= 2 and not 1 <= parts[1] <= 12:
                    raise ValueError("Invalid event month")
                if len(parts) == 3:
                    date.fromisoformat(e["date"])
                if not years[0] <= parts[0] <= years[-1]:
                    raise ValueError("Event date must fall within its year or year range")
            strings(e["models"], "models")
            strings(e["reported_evidence"], "reported_evidence")
            if set(e["reported_evidence"]) - set(EVIDENCE):
                raise ValueError("Unknown evidence label")
            if e["reviewed_on"] is not None:
                date.fromisoformat(e["reviewed_on"])
            if not isinstance(e["links"], list) or not e["links"]:
                raise ValueError("An event needs source links")
            for link in e["links"]:
                if set(link) != {"label", "url", "type"}:
                    raise ValueError("Invalid link fields")
                parsed = urlparse(link["url"])
                if parsed.scheme not in ("https", "http") or not parsed.netloc:
                    raise ValueError("Unsafe URL")
                if not link["label"] or link["type"] not in [
                    "Paper",
                    "Code",
                    "Lean",
                    "Formal proof",
                    "News",
                    "Context",
                ]:
                    raise ValueError("Invalid link")


def esc(s):
    return html.escape(str(s), quote=True)


def rich(text):
    parts, pos = [], 0
    for match in LINK.finditer(text):
        parts += [esc(text[pos : match.start()]), f'<a href="{esc(match[2])}">{esc(match[1])}</a>']
        pos = match.end()
    parts.append(esc(text[pos:]))
    rendered = re.sub(r"`([^`]+)`", r"<code>\1</code>", "".join(parts))
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", rendered)


def text_blocks(text):
    out = []
    for block in text.strip().split("\n\n"):
        if block.startswith("# "):
            out.append(f"<h2>{esc(block[2:])}</h2>")
        elif block.startswith("## "):
            out.append(f"<h3>{esc(block[3:])}</h3>")
        elif block.startswith("- "):
            out.append("<ul>" + "".join(f"<li>{rich(line[2:])}</li>" for line in block.splitlines()) + "</ul>")
        else:
            out.append(f"<p>{rich(block)}</p>")
    return "".join(out)


def models(p):
    return list(dict.fromkeys(m for e in p["events"] for m in e["models"]))


def statuses(p):
    return [s for s in EVIDENCE if any(s in e["reported_evidence"] for e in p["events"])]


def year(p):
    years = [int(y) for e in p["events"] for y in e["year"].split("-")]
    return str(min(years)) if min(years) == max(years) else f"{min(years)}–{max(years)}"


def date_key(value):
    """Return a sortable ISO-like key; unknown month/day sort before known ones."""
    if re.fullmatch(r"\d{4}-\d{4}", value):
        value = value.split("-")[-1]
    parts = value.split("-")
    return f'{parts[0]}-{parts[1] if len(parts)>1 else "00"}-{parts[2] if len(parts)>2 else "00"}'


def event_date(e):
    return e.get("date", e["year"])


def format_date(value):
    if re.fullmatch(r"\d{4}-\d{4}", value):
        return value.replace("-", "–")
    parts = value.split("-")
    if len(parts) == 1:
        return value
    month = date(int(parts[0]), int(parts[1]), 1).strftime("%b")
    if len(parts) == 2:
        return f"{month} {parts[0]}"
    return f"{month} {int(parts[2])}, {parts[0]}"


def problem_date(p):
    values = sorted({event_date(e) for e in p["events"]}, key=date_key)
    if len(values) == 1:
        return format_date(values[0])
    return f"{format_date(values[0])}–{format_date(values[-1])}"


def problem_date_key(p):
    return max(date_key(event_date(e)) for e in p["events"])


def mdcell(s):
    return s.replace("|", "\\|").replace("\n", " ")


def badge(status, scope="result", context=""):
    symbol = (
        "⚑"
        if status in ["verified", "debunked"]
        else "✓" if status == "machine-checked" else "!" if status == "disputed" else "•"
    )
    label = status + (f" ({scope})" if scope != "result" else "")
    return f'<span class="badge {esc(status)}" title="{esc(context or label)}"><span class="flag" aria-hidden="true">{symbol}</span>{esc(label)}</span>'


def problem_badges(p):
    result = []
    for status in EVIDENCE:
        scopes = list(dict.fromkeys(e["evidence_scope"] for e in p["events"] if status in e["reported_evidence"]))
        for scope in scopes:
            events = [
                e["title"] for e in p["events"] if status in e["reported_evidence"] and e["evidence_scope"] == scope
            ]
            result.append(badge(status, scope, "; ".join(events)))
    return '<div class="badges">' + "".join(result) + "</div>"


def refs(p, markdown=False):
    seen, out = set(), []
    for e in p["events"]:
        for link in e["links"]:
            if link["url"] in seen:
                continue
            seen.add(link["url"])
            if markdown:
                out.append(f'[{link["type"]}]({link["url"]})')
            else:
                out.append(
                    f'<a class="source" href="{esc(link["url"])}" title="{esc(link["label"])}">{esc(link["type"])} ↗<span class="sr-only">: {esc(link["label"])}</span></a>'
                )
    return " · ".join(out) if markdown else "".join(out)


def page(title, body, prefix=""):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)} · Awesome AI Proofs</title><meta name="description" content="AI-assisted mathematics and statistics, organized by problem with sources, models and reported verification status."><link rel="icon" href="data:,"><link rel="stylesheet" href="{prefix}assets/style.css"><script src="{prefix}assets/catalogue.js" defer></script><script src="{prefix}assets/app.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="{prefix}index.html">AWESOME AI PROOFS</a><nav aria-label="Main"><a href="{prefix}index.html">Problems</a><a href="{prefix}visualizations.html">Visualizations</a><a href="{REPO}/blob/main/CONTRIBUTING.md">Contribute ↗</a><a href="{REPO}">GitHub ↗</a></nav></header><main id="main">{body}</main><footer>Awesome AI Proofs<span><a href="{REPO}/blob/dev/LICENSE">MIT licence</a> · <a href="{REPO}">Source repository</a></span></footer></body></html>"""


def event_html(e):
    badges = "".join(badge(s, e["evidence_scope"]) for s in e["reported_evidence"])
    review = "Source read " + e["reviewed_on"] if e["reviewed_on"] else "Source review pending"
    links = "".join(f'<li><a href="{esc(l["url"])}">{esc(l["type"])} — {esc(l["label"])}</a></li>' for l in e["links"])
    return f'<article class="event"><div class="eyebrow">{esc(format_date(event_date(e)))}</div><h2>{esc(e["title"])}</h2><p class="event-model"><strong>Model / AI:</strong> {esc(", ".join(e["models"]))}</p><div class="badges">{badges}</div><p>{rich(e["summary"])}</p><p class="review"><strong>{esc(review)}.</strong> {esc(e["review_note"])}</p><ul class="event-links">{links}</ul></article>'


def chart_records(items):
    return [
        dict(
            id=p["id"],
            title=p["title"],
            category=p["category"],
            subjects=p["subjects"],
            models=models(p),
            evidence=statuses(p),
            years=sorted({e["year"].split("-")[-1] for e in p["events"]}),
        )
        for p in items
    ]


def counts(records, dimension):
    return sorted(
        Counter(v for p in records for v in set(p[dimension])).items(),
        key=(lambda kv: int(kv[0])) if dimension == "years" else (lambda kv: (-kv[1], kv[0])),
    )


def chart_markup(records, dimension):
    values = counts(records, dimension)
    maximum = max([v for _, v in values], default=1)
    return "".join(
        f'<a class="chart-bar {esc(label) if dimension=="evidence" else ""}" href="#chart-records" data-dimension="{dimension}" data-value="{esc(label)}" aria-label="{esc(label)}: {n} records"><span class="bar-label">{esc(label)}</span><span class="bar-track"><span style="width:{n/maximum*100:.4f}%"></span></span><strong>{n}</strong></a>'
        for label, n in values
    )


def viz_page(items):
    records = chart_records(items)
    panels = []
    for dimension, title, sub in [
        ("years", "Records by year", "Year of the reported event; ranges use their final year."),
        ("evidence", "Reported evidence", "A record can have more than one status."),
        ("models", "Models and AI systems", "A record can credit several systems."),
        ("subjects", "Mathematical subjects", "A record can belong to several subjects."),
    ]:
        panels.append(
            f'<section class="chart-panel"><h2>{title}</h2><p>{sub}</p><div class="chart-bars" id="chart-{dimension}">{chart_markup(records,dimension)}</div></section>'
        )
    docs = (ROOT / "docs/visualizations.md").read_text()
    explanations = []
    for p in items:
        path = ROOT / f'explanations/{p["id"]}.md'
        if path.exists():
            explanations.append(
                f'<details id="explanation-{p["id"]}" class="documentation"><summary>{esc(p["title"])}</summary>{text_blocks(path.read_text())}<a href="problems/{p["id"]}.html">Problem and sources →</a></details>'
            )
    resource_docs = text_blocks((ROOT / "docs/resources.md").read_text())
    rows = "".join(
        f'<li data-record="{p["id"]}"><a href="problems/{p["id"]}.html">{esc(p["title"])}</a><span>{esc(year(p))} · {esc(p["category"])}</span></li>'
        for p in items
    )
    payload = (
        json.dumps(records, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    )
    return f"""<section class="page-heading"><div class="eyebrow">Mathematics & statistics</div><h1>Catalogue overview</h1><p class="lede">Explore the listed problems by year, subject, model and reported evidence.</p></section><div class="viz-toolbar"><label>Type<select id="viz-category"><option value="">All types</option>{''.join(f'<option>{c}</option>' for c in CATEGORIES)}</select></label><p id="viz-count" role="status">{len(records)} records</p><button id="viz-reset" type="button">Reset selection</button></div><p class="chart-note">Counts describe this catalogue, not model success rates. Select a bar to see its records. Status and model counts can overlap.</p><div class="chart-grid">{''.join(panels)}</div><section id="chart-records"><div class="catalogue-heading"><h2 id="selection-title">All records</h2><span id="selection-count" role="status">{len(records)} records</span></div><ul class="chart-records">{rows}</ul></section><section class="documentation-section" id="documentation"><h2>Definitions and documentation</h2>{text_blocks(docs)}<h3>Problem explanations</h3>{''.join(explanations)}<details class="documentation" id="resources"><summary>Tools, benchmarks and related links</summary>{resource_docs}</details></section><script type="application/json" id="chart-data">{payload}</script>"""


def generate():
    items = load_problems()
    outputs = {}
    md = (ROOT / "docs/readme-intro.md").read_text() + "\n"
    for cat in CATEGORIES:
        md += f"## {LABELS[cat]}\n\n| Problem / reported evidence | Subject / tags | Model / AI | Date / year | Links | Additional information |\n| --- | --- | --- | --- | --- | --- |\n"
        for p in (p for p in items if p["category"] == cat):
            marks = " · ".join(("⚑ " if s in ["verified", "debunked"] else "") + s for s in statuses(p))
            md += f'| [{mdcell(p["title"])}](problems/{p["id"]}.md)<br>{marks} | {", ".join(p["subjects"])} | {mdcell(", ".join(models(p)))} | {problem_date(p)} | {refs(p,True)} | {mdcell(p["caveat"])} |\n'
        md += "\n"
    md += "## Contributing\n\nAdd problems in a YAML file under `data/problems/`. See [CONTRIBUTING.md](CONTRIBUTING.md) for the format, checks and publishing instructions.\n\n## Acknowledgements\n\nInspired by [awesome-ai-for-math](https://github.com/seewoo5/awesome-ai-for-math). The starting notes acknowledge Alexander Kruel’s [AI Systems as Generators of Novel and Valuable Work](https://drive.google.com/file/d/1zZquxGHisonG8-ukMTr9frPjJkSd0s_l/). The [original notes](archive/original-notes.md) are retained as an archive.\n"
    outputs["README.md"] = md
    rows = []
    for p in items:
        explanation = ROOT / f'explanations/{p["id"]}.md'
        detail = f'# {p["title"]}\n\n[← Problems](../README.md) · [Definitions and documentation](../docs/visualizations.md)\n\n**{p["category"]} · {", ".join(p["subjects"])} · {problem_date(p)}**\n\n**Model / AI:** {", ".join(models(p))}\n\n## Question\n\n{p["question"]}\n\n## Additional information\n\n{p["caveat"]}\n\n'
        if explanation.exists():
            detail += f'[Problem explanation](../explanations/{p["id"]}.md)\n\n'
        for e in p["events"]:
            detail += f'## {format_date(event_date(e))} · {e["title"]}\n\n**Model / AI:** {", ".join(e["models"])}\n\n{e["summary"]}\n\n**Reported evidence ({e["evidence_scope"]}):** {", ".join(e["reported_evidence"])}.\n\n**Source review:** {e["reviewed_on"] or "Pending"}. {e["review_note"]}\n\n'
            detail += "\n".join(f'- [{l["type"]} — {l["label"]}]({l["url"]})' for l in e["links"]) + "\n\n"
        outputs[f'problems/{p["id"]}.md'] = detail
        body = f'<a class="back" href="../index.html">← Problems</a><div class="eyebrow">{esc(p["category"])} / {esc(problem_date(p))}</div><h1>{esc(p["title"])}</h1><p class="lede">{esc(p["question"])}</p><p><strong>Model / AI:</strong> {esc(", ".join(models(p)))}</p>{problem_badges(p)}<aside class="caveat">{esc(p["caveat"])}</aside>'
        if explanation.exists():
            body += f'<p><a href="../visualizations.html#explanation-{p["id"]}">Problem explanation →</a></p>'
        body += "".join(event_html(e) for e in p["events"])
        outputs[f'docs-site/problems/{p["id"]}.html'] = page(p["title"], f'<div class="reading">{body}</div>', "../")
        search = " ".join(
            [
                p["title"],
                *p["subjects"],
                *models(p),
                p["question"],
                p["caveat"],
                *[e["title"] + " " + e["summary"] for e in p["events"]],
            ]
        )
        rows.append(
            f"""<tr data-category="{esc(p['category'])}" data-subjects="{esc(json.dumps(p['subjects']))}" data-models="{esc(json.dumps(models(p)))}" data-evidence="{' '.join(statuses(p))}" data-date="{problem_date_key(p)}" data-search="{esc(search)}"><th scope="row"><span class="row-kind">{esc(p['category'])}</span><a class="problem-title" href="problems/{p['id']}.html">{esc(p['title'])}</a>{problem_badges(p)}</th><td><div class="tags">{''.join(f'<span>{esc(s)}</span>' for s in p['subjects'])}</div></td><td class="models">{''.join(f'<span>{esc(m)}</span>' for m in models(p))}</td><td class="year">{esc(problem_date(p))}</td><td><div class="sources">{refs(p)}</div></td><td><details class="row-details"><summary title="{esc(p['caveat'])}">Details</summary><p>{esc(p['caveat'])}</p><a href="problems/{p['id']}.html">Attempts and sources →</a></details></td></tr>"""
        )
    template = (ROOT / "site/index.html").read_text()
    substitutions = {
        "ROWS": "".join(rows),
        "SUBJECTS": "".join(f"<option>{esc(s)}</option>" for s in sorted({s for p in items for s in p["subjects"]})),
        "MODELS": "".join(f"<option>{esc(m)}</option>" for m in sorted({m for p in items for m in models(p)})),
        "COUNT": str(len(items)),
    }
    for key, value in substitutions.items():
        template = template.replace("{{" + key + "}}", value)
    outputs["docs-site/index.html"] = page("Problems", template)
    outputs["docs-site/visualizations.html"] = page("Visualizations", viz_page(items))
    for name in ["style.css", "app.js", "catalogue.js"]:
        outputs["docs-site/assets/" + name] = (ROOT / "site" / name).read_text()
    outputs["docs-site/.nojekyll"] = ""
    return outputs


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        outputs = generate()
    except ValueError as error:
        parser.exit(1, str(error) + "\n")
    stale = []
    for name, content in outputs.items():
        dest = ROOT / name
        if args.check:
            if not dest.exists() or dest.read_text() != content:
                stale.append(name)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content)
    for folder, pattern in [("problems", "*.md"), ("docs-site/problems", "*.html")]:
        for dest in (ROOT / folder).glob(pattern):
            if str(dest.relative_to(ROOT)) not in outputs:
                if args.check:
                    stale.append(str(dest.relative_to(ROOT)))
                else:
                    dest.unlink()
    if stale:
        parser.exit(1, "Generated files are stale: " + ", ".join(stale) + "\n")
    print(f'{"Checked" if args.check else "Generated"} {len(outputs)} files; YAML catalogue valid.')
