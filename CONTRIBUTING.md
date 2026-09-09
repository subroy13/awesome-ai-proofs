# Contributing

Add a mathematical problem, update an attempt, or correct a source or attribution.

## Add a YAML file

Create a `.yaml` or `.yml` file anywhere under `data/problems/`. You may use your GitHub handle or a topic in the filename, and include multiple problems in one file. The build reads this folder recursively in a deterministic order.

Search existing files first. Every problem ID must be unique across the folder. For another attempt at an existing problem, edit that problem’s events rather than duplicating its ID in your file. Files are organizational choices, not mathematical authorship credits. The optional top-level `contributor` field identifies the curator.

```yaml
contributor: your-github-handle
problems:
  - id: descriptive-problem-id
    title: Name of the mathematical problem
    subjects: [Probability, Statistics]
    category: Research
    question: A precise or intuitive statement with essential assumptions.
    caveat: Which cases or proof steps remain unchecked?
    events:
      - title: A specific attempt or result
        year: '2026'
        date: '2026-09-08'
        models: [Model name]
        summary: What was obtained, what AI did, and what humans did.
        evidence_scope: result
        reported_evidence: [self-reported]
        reviewed_on: null
        review_note: Source review pending.
        links:
          - label: Original paper
            url: https://example.org/paper
            type: Paper
```

Replace the example content with a real statement and supporting sources. The build rejects duplicate IDs, duplicate YAML keys, unsafe tags, missing fields and unsupported categories. An optional event `source_group` identifies a shared study when several problems come from the same study.

## Content rules

- Categories are `Research`, `Competitions` and `Historical`. Failed attempts, corrections, disputes and evaluation questions belong under Research. Split multi-result papers into individual problems or precisely identified variants.
- Keep titles problem-centric. Use a short description of the mathematical claim, followed by its identifier where applicable, such as `Odd squares as XORs of consecutive squares (OEIS A224515)`. Distinguish separate claims about the same sequence; avoid titles consisting only of an identifier and conjecture number. List AI systems in `models`, using a company name for an unreleased system where appropriate. Use `Not specified` when attribution is unavailable; never guess a model.
- Describe human contributions in `summary`. Distinguish new proofs, formalizations, partial results, rediscoveries and invalid claims.
- Keep the language factual. Omit slogans, “Lesson:” sentences and unsupported priority claims.
- Evidence labels are `verified`, `machine-checked`, `self-reported`, `disputed` and `debunked`. Multiple labels can apply to the same attempt. `evidence_scope` names what the label concerns, such as `result`, `audit` or `novelty claim`.
- Include a source for corrections and criticism, not only the initial announcement. Prefer primary papers, author repositories and maintainer postmortems. News can provide additional context.
- Link types are `Paper`, `Lean`, `Formal proof`, `Code`, `News` and `Context`. A code repository alone does not establish formal verification.
- For formal artifacts, record the precise theorem, file, revision, tool version, assumptions and verified scope in the summary or caveat. State when a build or statement audit has not been performed.
- Use a year or ordered year range (`2026`, `'2024-2025'`). Add optional `date` as `YYYY-MM` or `YYYY-MM-DD` when the first public report or source publication date is known; do not infer a day. Table ordering uses this date and falls back to the year. A quoted date or ordinary YAML date is accepted for both `date` and `reviewed_on`. Source reading is distinct from proof verification; say exactly what was read in `review_note`.

The [visualization documentation](docs/visualizations.md) defines labels and counting rules. Longer intuitive explanations go in `explanations/<problem-id>.md` and appear under Visualizations. Use paragraphs, `##` headings, HTTP(S) Markdown links and inline code. Tools and other supporting links live in `docs/resources.md`; there is no resources dataset.

## Build and test

Use Python 3.10+ and Node.js 18+. Install the pinned YAML parser in a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build.py
.venv/bin/python scripts/build.py --check
.venv/bin/python -m unittest discover -s tests
node tests/test_filters.js
```

Commit the edited YAML and generated files together. `README.md`, `problems/` and `docs-site/` are generated; edit `docs/readme-intro.md`, `docs/visualizations.md`, the YAML files or `site/` instead. The original notes remain unchanged in `archive/` as historical source material.

## Preview and publish

```sh
python3 -m http.server 8000 --directory docs-site
```

Open http://localhost:8000. All problem rows, links and chart values are included in the generated HTML. Interactive filtering and chart selections require JavaScript.

Pull requests run checks without publishing. To deploy, enable **Settings → Pages → Source: GitHub Actions** and allow `dev` in the `github-pages` environment’s branch rules. A push to `dev` runs **Publish catalogue**. Manual dispatch is also available once the workflow exists on the default branch. See [GitHub’s documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

You can also suggest an entry through the issue template. Submit focused changes and describe the sources and checks performed. Contributions use the repository’s MIT licence; linked works retain their own licences.
