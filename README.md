# Repository — Mapping the Measurement of Engineering Competencies: A Bibliometric Review of Technical and Transversal Constructs, 2014-2026

Segundo Francisco Segura Altamirano, Bertila Hernandez Fernandez
Universidad Cesar Vallejo, Pimentel, Peru

This repository documents the full research trail behind the manuscript submitted to the *European Journal of Engineering Education* (EJEE) — from the review protocol through database search, deduplication, screening, and every bibliometric analysis output, in addition to the manuscript itself. It supports the article's Data Availability Statement and the journal's Data Sharing Policy.


## Contents, in research-process order

### `00_review_protocol/`
- `propuestaCadA.txt` — the review protocol: title, domain, PCC question framework, full Scopus search string, scope of review, core-construct and near-miss definitions, inclusion/exclusion criteria, uncertainty-handling rule, and calibration anchors used to guide screening.

### `01_database_search/`
Raw, unmodified export files from each of the six databases searched, as retrieved:
- `scopusCadA.ris`, `wosCadA.ris`, `DimensionsCadA.ris` — Scopus, Web of Science, Dimensions.
- `ebscoCadA_01.bibtex`, `ebscoCadA_02.bibtex`, `ebscoCadA_03.bibtex` — EBSCOhost (split across export batches).
- `ericCadA.nbib` — ERIC.
- `ieeeCadA_01.bib`, `ieeeCadA_02.bib`, `ieeeCadA_03.bib` — IEEE Xplore (split across export batches).

### `02_deduplication/`
- `dedup_report.txt` — summary report: 1,193 raw records → 906 unique after DOI-match (207 pairs) and fuzzy-title (77 pairs) deduplication, plus per-source overlap counts and metadata-completeness statistics.
- `consolidado_deduplicado.ris`, `consolidado_CadA.ris`, `consolidadoCadA.csv` — the consolidated, deduplicated record sets at various stages.
- `Incluidos_CadA.csv`, `Incluidos_CadA.ris`, `Incluidos_CadAFinal.csv`, `cadenaAIncluidos.csv` — included-record subsets at different pipeline checkpoints.
- `stage1_terminological_snowballCadA.csv`, `snowball_candidatos_cadA.csv`, `snowball_candidatos_cadA_contrato.csv`, `cadeA_Snowballing.csv`, `snowball_log.txt`, `snowball_openalex.py`, `snowball_stage1_only.py` — citation-snowballing candidates (via OpenAlex) and the scripts used to generate them.
- `chatgptCodificacion.txt`, `chatgptCodificacionCompleta.txt`, `gemini-code-1784782612082.json`, `promptAnalisisTematicoInductivo.txt` — LLM-assisted coding session records referenced in the Methodology's triangulation step.

### `03_screening/`
- `cadenaAIncluidos.csv` — final included-record list for this review chain.
- `screening_trace_20260722_000511.csv` and `screening_trace_20260722_000511_UserDecision.csv` — the full per-record two-stage screening trace: Stage 1 (deterministic terminological filter) and Stage 2 (three-AI-agent semantic panel — principal investigator / methodologist / domain expert roles — with per-reviewer decision, score, criterion, evidence quote, and justification; unanimity required, any split routed to human review). The `_UserDecision` file is the version with human adjudication of uncertain cases applied, and is the source for the PRISMA numbers reported in the Methodology. This stage produced 97 screening-level includes; one near-duplicate pair was consolidated into a single record during final corpus assembly, yielding the 96-article corpus used throughout the manuscript (see `02_deduplication/dedup_report.txt` and `data/resultados_corpus_96articles.bib`).
- `review_design_report_20260722_000511.md`, `review_design_results_20260722_000511.json` — the downstream review-design synthesis (objective, PCC question, coverage matrix) generated from the screened corpus.
- `trace_20260722_000511.json` — machine-readable screening trace log.
- `stage1_terminological_20260722_003445.csv` (**note:** intentionally *not* included here — that timestamp corresponds to cadena B's session, not this review).

### `04_bibliometric_analysis_outputs/`
Full output of the bibliometric and thematic analysis pipeline's corrected run (mirrors the project's `output/` folder in its entirety, 697 files, corpus N=96), including:
- `figures/`, `networks/`, `plotly/` — all generated charts and interactive network visualizations.
- `citespace/`, `vosviewer/` — tool-specific exports from the co-citation/coupling network software. **Note:** `citespace/citespace_report.md` reports co-citation network modularity Q=0.14 and mean silhouette S=0.09, both below the report's own thresholds for a well-separated clustering solution (Q>0.3, S>0.7); the manuscript's Discussion discloses this as a limitation on the "three thematic clusters" reading of Figure 5.
- `leiden/`, `impact_evolution/` — normalized citation-impact indicators (FWCI, MNCS, Leiden rankings, sleeping-beauty/beauty-coefficient analysis, Citation Success Symbol classification). `leiden/leiden_summary.md` explicitly notes that per-field MNCS values are ≈1.0 by mathematical construction and are not suitable for comparing fields to each other — only the corpus-wide MNCS (0.927) is used comparatively in the manuscript.
- `rdm/` — Research Dynamics Manifold data and visualizations (Emergence/Impact/Connectivity axes, 8 archetypes).
- `spectroscopy/` — reference-publication-year spectroscopy (RPYS) and concept co-citation/lifecycle data.
- `inductive/`, `triangulation/` — LLM-assisted inductive thematic analysis results and the cross-model (DeepSeek vs. Gemini vs. ChatGPT) triangulation check. Multiple timestamped re-runs are retained for audit purposes; the manuscript's thematic-size claims (e.g., "~30 studies", "~22 studies") are drawn from the most recent run.
- `sota_analysis/` — LLM-assisted research-gap and method×domain coverage extraction; underlies the "declared and structural gaps" content in Results.
- `oa_corpus/` — open-access status classification of the corpus.
- `population_analysis/`, `population_sample/`, `quality/` — sample-size, discipline/geographic, and abstract/metadata quality analyses.
- `knowledge_map/` — the structural plans and condensed/extended drafts for Introduction, Methodology, Results, and Discussion generated from the synthesis data. These are working scaffolding, superseded in their numbers and phrasing by the final manuscript text in `manuscript/`.
- `bib_alt_triangulation/`, `reports/`, `reproducibility/`, `logs/` — supporting cross-checks (including a citation-vs-altmetric triangulation not yet incorporated into the manuscript body), descriptive/EDA reports, bootstrap confidence-interval checks, and run logs.
- `bibliometrix_analysis.R`, `bibliometrix_export.bib`, `bibliometrix_export.csv` — the R/Bibliometrix-side analysis script and its data export (96 entries).
- `SESSION_STATUS_2026-07-23.md` — a dated snapshot note from an earlier point in the analysis pipeline's history; retained for audit trail. Its corpus-size figure (97) reflects the pipeline's state at that specific moment, before the near-duplicate consolidation described above — see `data/resultados_corpus_96articles.bib` and the Methodology for the final, corrected count.

### `data/`
- `resultados_corpus_96articles.bib` — the core dataset: full bibliographic metadata for the 96 articles composing the reviewed corpus. This is the file used for the manuscript's citations.
- `biblioArticulo_supporting_literature.bib` — the 71 supporting-literature references cited in the manuscript's Introduction, Methodology, Results, and Discussion (i.e., everything in the reference list that is *not* one of the 96 reviewed articles) — including the classic method references (Bandura x4, Kline, Bradford, Lotka, Price, Louvain/Blondel et al., CiteSpace/Chen).
- `dedup_report_cadA.txt`, `screening_trace_PRISMA.csv` — copies of the deduplication and screening trace files also present in `02_deduplication/` and `03_screening/`, gathered here for convenience when reproducing only the citation/PRISMA numbers without the full pipeline tree.

### `manuscript/`
- `manuscript_EN_v2.docx` — full manuscript (Word), assembled in EJEE's required order.
- `manuscript_EN_v2.md` — the same manuscript in Markdown (Pandoc + citeproc source).

This is the manuscript's second full draft. Human co-author review of the LLM-assisted Results, Discussion, and Conclusions text is still pending at the time of this snapshot — see "Known open items" below and the manuscript's own Declaration of Generative AI Use.

### `figures/`
The 11 figures used in the manuscript (3 in Methodology, 8 in Results — Figure 9 has two panels, a/b), sequentially renamed to match in-text callouts, all at high resolution:
- Figures 1-3 (Methodology): PRISMA-style search/screening flow diagram, an overview of the nine-phase analytical pipeline, and the three-phase inductive thematic analysis workflow — rendered from the Mermaid sources in `docs/` at the project root.
- Figures 4-10 (Results): rendered from `04_bibliometric_analysis_outputs/` (annual growth, co-citation network, SCP/MCP collaboration, thematic map, keyword-trend bursts, FWCI histogram, beauty-coefficient scatter, RDM 3D manifold).

### `appendices/`
- `appendix_included_studies.docx` — Appendix A: the 96 included studies as a numbered APA reference list.
- `appendix_included_studies_table.docx` — Appendix B: the same 96 studies as a table (#, Author(s)/Year, Title, Source, DOI).

Both were verified against `data/resultados_corpus_96articles.bib` at this snapshot (96/96 entries matched, including disambiguation of same-surname authors).

### `supplementary/`
- `Figure_10_rdm_manifold_3d_interactive.html` — interactive (Plotly) version of Figure 10 (Research Dynamics Manifold), for online/digital readers, generated from the same corrected N=96 run as the static figure.
