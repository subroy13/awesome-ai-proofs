# LLM Guide to Awesome AI Proofs

This document serves as the comprehensive context guide for Large Language Models (LLMs) and automated agents interacting with, contributing to, or analyzing the `awesome-ai-proofs` repository.

---

## 1. Executive Summary & Philosophy

`awesome-ai-proofs` is a rigorous, curated catalogue of AI-assisted results across pure mathematics, applied mathematics, statistics, and theoretical computer science.

### Core Distinctions
- **Problem-Centric, Not Model-Centric:** Entries are structured around the specific *mathematical problem, conjecture, or theorem*, rather than around model release cycles or corporate marketing claims. Multiple attempts across different years and systems on the same problem reside under one entry.
- **Evidence-Based & Nuanced:** Results are tagged with granular reported evidence labels (`verified`, `machine-checked`, `self-reported`, `disputed`, `debunked`) along with an explicit `evidence_scope` (e.g., `result`, `audit`, `novelty claim`).
- **Separation of Source Reading from Proof Auditing:** The catalogue documents whether maintainers have read the source paper/artifact (`reviewed_on`, `review_note`), while explicitly clarifying that inclusion does *not* constitute an independent verification or re-formalization audit by this repository.
- **Inclusion of Caveats & Failures:** Partial results, autoformalizations resting on unformalized classical inputs, compiler-trusted steps (`native_decide`), unverified cases, retracted announcements, and benchmark evaluation errors are documented alongside positive breakthroughs.
- **Objective, Non-Sensationalist Tone:** Slogans, lessons, hype, marketing prose, and unsubstantiated priority claims are strictly forbidden and enforced by CI test suites.

---

## 2. Repository Architecture: Source of Truth vs. Generated Artifacts

**CRITICAL INVARIANT:** This repository uses a generator pipeline. Never edit generated files directly; any edits must be made to the source data or templates, followed by executing the build script.

```
awesome-ai-proofs/
├── data/
│   └── problems/                 <-- [SOURCE OF TRUTH] Problem database (YAML)
│       ├── additional-sources.yaml
│       ├── banach-spaces.yaml
│       ├── core.yaml
│       ├── erdos.yaml
│       ├── kourovka.yaml
│       ├── oeis.yaml
│       ├── openai-math-lean.yaml
│       ├── openai-results.yaml
│       ├── research-additions-2026-09.yaml
│       └── research-additions-2026-10.yaml
├── docs/                         <-- [SOURCE OF TRUTH] Hand-written documentation
│   ├── readme-intro.md           # Markdown introduction header for root README.md
│   ├── visualizations.md         # Documentation displayed on visualizations page
│   └── resources.md              # Curated tools, provers, and benchmarks
├── explanations/                 <-- [SOURCE OF TRUTH] Intuitive math notes
│   ├── cap-sets.md               # Named <problem-id>.md; rendered into problem pages
│   ├── collatz-kernel.md
│   ├── feige.md
│   └── matrix-multiplication.md
├── site/                         <-- [SOURCE OF TRUTH] Frontend assets & templates
│   ├── index.html                # Template containing {{COUNT}}, {{SUBJECTS}}, etc.
│   ├── catalogue.js              # Pure domain logic: filter matching, record selection
│   ├── app.js                    # DOM event handlers, chart interactions, live filters
│   └── style.css                 # CSS stylesheet with dark/light theme tokens
├── archive/                      <-- [IMMUTABLE] Historical source material
│   └── original-notes.md         # Original unstructured list (referenced in regression tests)
├── scripts/                      <-- [TOOLING] Build and verification scripts
│   └── build.py                  # CLI build pipeline, validator, and renderer
├── tests/                        <-- [TOOLING] Automated test suites
│   ├── test_catalogue.py         # Python unit tests (integrity, schema, regression bans)
│   └── test_filters.js           # Headless DOM & filter tests run via Node.js
├── .github/                      <-- [CI/CD] GitHub Actions workflows & templates
│   ├── workflows/check.yml       # PR & push validation
│   ├── workflows/pages.yml       # GitHub Pages deployment pipeline
│   └── ISSUE_TEMPLATE/entry.md   # GitHub issue template for new problem proposals
│
│── [GENERATED ARTIFACTS - DO NOT DIRECTLY EDIT] ───────────────────────────
├── README.md                     <-- Generated: Main root catalogue markdown table
├── problems/                     <-- Generated: Individual Markdown files (<id>.md)
└── docs-site/                    <-- Generated: Static web build published to GitHub Pages
    ├── index.html                # Main searchable problem catalogue
    ├── visualizations.html       # Visual dashboard with interactive charts
    ├── assets/                   # Copied from site/ (style.css, app.js, catalogue.js)
    └── problems/                 # Generated standalone HTML pages (<id>.html)
```

---

## 3. Data Schema & Specification

All mathematical entries are defined in `.yaml` or `.yml` files located under `data/problems/`. The parser discovers all files recursively in deterministic lexicographical order.

### 3.1 Document-Level Structure
```yaml
contributor: optional-github-handle   # Optional curator identifier
problems:
  - id: sample-problem-id
    # ... problem fields ...
```

### 3.2 Problem-Level Schema
Each problem mapping has **7 mandatory keys** (no extra keys permitted):

| Field | Type | Description & Validation Rules |
| :--- | :--- | :--- |
| `id` | `str` | Unique slug matching `^[a-z0-9]+(?:-[a-z0-9]+)*$`. Must be globally unique across all YAML files. |
| `title` | `str` | Short, descriptive mathematical claim or theorem name. Problem-centric. |
| `subjects` | `list[str]` | Non-empty list of mathematical subject areas (e.g., `[Graph theory, Combinatorics]`). |
| `category` | `str` | Must be exactly one of: `Research`, `Competitions`, `Historical`. |
| `question` | `str` | Precise or intuitive mathematical statement outlining core conditions and questions. |
| `caveat` | `str` | Critical limitations: unverified cases, assumptions, compiler trust (`native_decide`), scope gaps. |
| `events` | `list[dict]` | Non-empty list of chronological attempts or published results on this problem. |

### 3.3 Event-Level Schema
Each event under `events` represents an attempt, proof, disproof, or evaluation:

| Field | Type | Required? | Constraints & Details |
| :--- | :--- | :---: | :--- |
| `title` | `str` | Yes | Title of this specific attempt or publication. |
| `year` | `str` | Yes | Year string: `YYYY` or ordered range `YYYY-YYYY` (e.g. `'2024-2025'`). Unquoted integers are normalized to strings. |
| `date` | `str` | No | Precise date string: `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`. Must fall within the designated `year` or `year` range. |
| `models` | `list[str]` | Yes | Non-empty list of AI models or systems credited (e.g. `[AlphaProof, AlphaGeometry 2]`, `[GPT-5.4 Pro]`, `[OpenAI (unreleased)]`). Use `Not specified` if unknown. Never guess a model. |
| `summary` | `str` | Yes | Clear description of what was achieved, what the AI generated, and what human mathematicians contributed. |
| `evidence_scope` | `str` | Yes | What the evidence label applies to (e.g. `result`, `audit`, `novelty claim`). |
| `reported_evidence` | `list[str]` | Yes | Non-empty list containing only approved labels: `verified`, `machine-checked`, `self-reported`, `disputed`, `debunked`. |
| `reviewed_on` | `str` or `null` | Yes | `YYYY-MM-DD` string if a maintainer has read the source material; `null` if pending. |
| `review_note` | `str` | Yes | Factual report of what was read or checked (e.g., "Read the paper's knot-theory section; did not rerun Lean proof."). |
| `links` | `list[dict]` | Yes | Non-empty list of source link dictionaries (see below). |
| `source_group` | `str` | No | Optional identifier grouping related problems derived from a single paper or shared study. |

#### Link Specification
Each link dictionary inside an event's `links` list requires:
- `label`: `str` — Descriptive text (e.g., `Paper`, `Nature paper`, `Lean formalization`).
- `url`: `str` — Fully qualified HTTP/HTTPS URL (`http://` or `https://`).
- `type`: `str` — Must be one of: `Paper`, `Code`, `Lean`, `Formal proof`, `News`, `Context`.

---

## 4. Taxonomy of Evidence & Verification

The catalogue enforces rigorous terminology regarding AI mathematical achievements:

### Evidence Labels
1. **`verified`**: The result has been independently checked by qualified humans, external referees, or official competition coordinators (e.g., IMO coordinators, peer-reviewed journals).
2. **`machine-checked`**: A formal proof assistant (Lean, Coq, Isabelle, HOL Light) checked the formal statement against its axioms.
   - *Crucial Caveat:* Machine checking only verifies the formal statement as written. It does *not* prove that the formal statement correctly captures the informal open conjecture (statement fidelity requires human auditing).
   - *Compiler Trust:* Note if a proof relies on `native_decide` (trusted compiler execution) rather than the trusted kernel.
3. **`self-reported`**: The result, model capability, or evaluation score was claimed by the producing lab or authors without independent replication or peer verification.
4. **`disputed`**: Correctness, attribution, novelty, or formal statement correspondence is contested by external mathematicians or community postmortems.
5. **`debunked`**: The mathematical claim, proof step, or novelty claim was proven false, flawed, or retracted. (A debunked novelty claim does not necessarily imply the underlying mathematics was wrong).

### Categories
- **`Research`**: Genuine open research problems, conjectures, counterexamples, disproofs, and mathematical discoveries.
- **`Competitions`**: Olympiad-level or contest benchmarks (e.g., IMO, Putnam).
- **`Historical`**: Landmark historical computer-assisted proofs prior to modern LLMs (e.g., Four Color Theorem 1976, Robbins Conjecture 1996, Kepler Conjecture / Flyspeck 2014).

---

## 5. Build, Test, and Execution Pipeline

### Environment Setup
- Python: `3.10+` (CI runs Python `3.13`)
- Node.js: `18+`
- Python dependencies: `PyYAML==6.0.3` (see `requirements.txt`)

### Build Commands
```sh
# Generate all derived artifacts (README.md, problems/*.md, docs-site/*)
python3 scripts/build.py

# Validate consistency without writing (fails if any generated file is stale or YAML is invalid)
python3 scripts/build.py --check
```

### Test Commands
```sh
# Run Python unit tests (verifies link integrity, schema validation, regressions, and safety)
python3 -m unittest discover -s tests

# Run Node.js frontend tests (verifies table filters, live search, sorting, and charts)
node tests/test_filters.js

# Check syntax of core frontend JavaScript
node --check site/app.js
```

### Local Preview
```sh
# Serve the compiled static site locally
python3 -m http.server 8000 --directory docs-site
```

### Continuous Integration & Deployment
- `.github/workflows/check.yml`: Runs on PRs and pushes to `dev` and `main`. Executes `scripts/build.py --check`, python tests, and node filter tests.
- `.github/workflows/pages.yml`: Runs on pushes to `main` (and manual dispatch). Validates the build and deploys `docs-site/` directly to GitHub Pages.

---

## 6. Frontend & Web Architecture

The interactive catalogue (`docs-site/index.html` and `docs-site/visualizations.html`) is built with lightweight, dependency-free vanilla HTML/CSS/JavaScript.

1. **`site/catalogue.js` (Pure Logic Module):**
   - Universal module exported for both browser (`globalThis.Catalogue`) and Node.js (`module.exports`).
   - Implements `counts(records, dimension)`, `select(records, category, selection)`, and `matches(row, filters)`.
2. **`site/app.js` (DOM & Event Handling):**
   - Manages table filtering, fuzzy search over concatenated attributes (`data-search`), multi-parameter sorting (`newest`, `oldest`, `title`, `catalogue`), and record counting.
   - Manages the visualization dashboard: clicking any chart bar cross-filters the underlying problem records.
   - Deep-linking anchor support: automatically opens HTML5 `<details>` disclosure elements when navigating to their fragment identifier (e.g., `#explanation-<problem-id>`).
3. **`site/style.css`:**
   - Responsive CSS with clean mathematical typography, accessible color contrast, badge styling for verification statuses, and horizontal scroll tables for mobile viewports.

---

## 7. Mathematical & Historical Context

To generate accurate problem entries, an LLM should understand key concepts and developments documented in this repository:

- **Formal Verification Tools:** Lean 4 (`mathlib4`), Isabelle/HOL, Coq/Rocq, HOL Light. Most contemporary machine-checked proofs in this repo use Lean 4.
- **Notable AI Provers & Systems:**
  - *Google DeepMind:* AlphaTensor (matrix multiplication algorithms), FunSearch (cap sets), AlphaGeometry & AlphaGeometry 2 (olympiad geometry), AlphaProof (formal Lean proof search at IMO 2024), AlphaProof Nexus (Erdős and OEIS formal sweeps), AlphaEvolve.
  - *OpenAI:* OpenAI reasoning models (Sol / GPT-5-era models solving Erdős unit-distance conjecture, Cycle Double Cover conjecture, and 170+ research Lean formalizations).
  - *Anthropic:* Claude Opus 4.6 and Claude Fable 5 (Knuth's Hamiltonian cycles, Jacobian conjecture counterexample exploration, 2-adic absolute Galois group).
  - *Harmonic:* Aristotle (autonomous formal Lean group-theory proofs in the Kourovka Notebook, Erdős problem #728).
  - *Open Provers:* DeepSeek-Prover-V2, Goedel-Prover-V2, Kimina-Prover, Archon.
- **Leading Benchmarks & Initiatives:** miniF2F (and its audited v2), FrontierMath (Epoch AI), First Proof (research problems with blind refereeing), Formal Conjectures, PutnamBench, IMProofBench.

---

## 8. Editorial Guidelines & Style Rules for LLMs

When drafting, modifying, or reviewing problem entries:

1. **Strictly Neutral Language:**
   - Do NOT use marketing jargon, hype, or triumphant summaries (e.g., avoid "groundbreaking", "revolutionary", "stunning breakthrough").
   - Do NOT insert meta-commentary or pedagogical slogans like `Lesson: ...` or `A living catalogue`.
2. **Clarify Attribution & Collaboration:**
   - Clearly delineate what the AI generated (e.g. found an explicit counterexample coordinate, formulated a conjecture) vs. what humans contributed (e.g. formulated the problem, audited the Lean code, proved the general theorem from AI hints).
3. **Detail Verification Limitations:**
   - Always state if a formal proof has not been independently compiled from source by maintainers.
   - Detail any trusted compiler tactics (e.g. `native_decide`) or non-formalized classical lemmas upon which the theorem depends.
4. **Regression Invariants:**
   - Test suites explicitly search for and reject banned slogans and historical legacy strings:
     - `'A living catalogue'`
     - `'A proof has a scope'`
     - `'Lesson:'`
     - `'Reading the evidence'`
     - `'The good, the bad, and the QED'`
     - Legacy file paths like `data/problems.json` or `docs-site/guide.html`.

---

## 9. Step-by-Step Contribution Checklist for LLM Agents

When asked to add a new problem or modify an existing entry:

1. **Locate or Create YAML:**
   - Search existing files in `data/problems/` to ensure the problem does not already exist (e.g. grep by mathematical topic or identifier).
   - If adding to an existing problem, append a new event under its `events` list.
   - If creating a new problem, add it to the relevant `.yaml` file (or create a new descriptive YAML file under `data/problems/`).
2. **Fill Required Fields:**
   - Ensure all 7 problem fields and all required event fields are populated.
   - Use valid date formats (`YYYY`, `YYYY-MM`, or `YYYY-MM-DD`).
   - Use only valid `category`, `reported_evidence`, and link `type` strings.
3. **Optional Explanations:**
   - For complex mathematical results benefiting from intuitive exposition, add `explanations/<problem-id>.md`.
4. **Compile and Validate:**
   ```sh
   python3 scripts/build.py
   python3 scripts/build.py --check
   python3 -m unittest discover -s tests
   node tests/test_filters.js
   ```
5. **Commit Cleanly:**
   - Commit both the modified source YAML and the resulting generated files (`README.md`, `problems/<id>.md`, `docs-site/*`).
