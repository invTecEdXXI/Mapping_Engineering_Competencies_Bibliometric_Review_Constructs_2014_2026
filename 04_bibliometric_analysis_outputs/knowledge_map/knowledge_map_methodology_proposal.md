## Methodology — Structural Plan

### 1. Study Design and Review Framework

**Key points:**
- Define the review as a systematic bibliometric analysis combined with inductive thematic synthesis, designed to map the measurement instrument landscape in engineering education.
- Justify the mixed-methods design: bibliometric methods reveal structural patterns (productivity, collaboration, impact), while inductive thematic analysis captures conceptual content and emerging research fronts.
- Clarify that the design integrates descriptive, network, and semantic approaches within a single analytical pipeline, with triangulation across streams to strengthen validity.

**Feeds results sections:** S1, S2, S3, S4, S5, S6, S7, S8

**Scopus search string:** `TITLE-ABS-KEY("systematic review" AND "bibliometric" AND "engineering education") AND PUBYEAR > 2020`

**Estimated word count:** 120–150 words

---

### 2. Search Strategy and Corpus Construction

**Key points:**
- Database: Scopus (primary), supplemented by OpenAlex for metadata enrichment.
- Search string: the full Boolean string provided in the proposal (TITLE-ABS-KEY with four thematic blocks: engineering education, competencies, instruments, psychometric properties).
- Date range: 2014–2026; last search date: [specify].
- Inclusion criteria: peer-reviewed articles, conference papers, reviews in English or Spanish; focus on undergraduate/postgraduate engineering students; instruments measuring technical or transversal competencies.
- Exclusion criteria: non-engineering populations, non-measurement studies, opinion pieces, editorials.
- Deduplication: automated (Scopus ID) plus manual check.
- Final corpus: 96 articles.

**Feeds results sections:** S1 (corpus profile), S2 (intellectual structure)

**Scopus search string:** `TITLE-ABS-KEY("systematic review" AND "search strategy" AND "Scopus" AND "engineering") AND PUBYEAR > 2020`

**Estimated word count:** 180–220 words

---

### 3. Data Extraction and Multi-Source Enrichment

**Key points:**
- Primary source: Scopus (title, abstract, keywords, author affiliations, citations, references).
- Supplementary enrichment: OpenAlex (enhanced citation counts, topic classification, concept tags); Crossref (DOI resolution, funding data); Semantic Scholar (influence scores, TLDR abstracts); Altmetric (social media attention, policy mentions).
- Harmonization: author name disambiguation (OpenAlex ID), journal name normalization, year standardization.
- Export fields: full bibliographic record, cited references, author keywords, Index Keywords, funding information, citation counts.

**Feeds results sections:** S1 (corpus profile), S2 (intellectual structure), S3 (social structure), S4 (conceptual structure), S7 (impact indicators)

**Scopus search string:** `TITLE-ABS-KEY("data enrichment" AND "bibliometric" AND "OpenAlex") AND PUBYEAR > 2020`

**Estimated word count:** 150–180 words

---

### 4. Descriptive Bibliometric Analysis

**Key points:**
- Core indicators: publication growth trajectory (CAGR), Bradford's law (core journals), Lotka's law (author productivity), Zipf's law (keyword frequency), Price's law (citation concentration).
- Tools: custom Python scripts (NumPy, SciPy) for distribution fitting; visualization via Matplotlib/Seaborn.
- Outputs: annual publication counts, journal concentration curve, author productivity distribution, keyword frequency rank, citation distribution.
- These analyses provide the foundational descriptive profile of the field.

**Feeds results sections:** S1 (corpus profile), S4 (conceptual structure)

**Scopus search string:** `TITLE-ABS-KEY("Bradford's law" AND "bibliometric" AND "engineering education") AND PUBYEAR > 2020`

**Estimated word count:** 130–160 words

---

### 5. Network Analysis: Co-Citation, Coupling, and Co-Authorship

**Key points:**
- Co-citation analysis: document co-citation network to identify intellectual foundations (seminal works, research schools). Threshold: top 50 most cited references; pruning: pathfinder network scaling.
- Bibliographic coupling: document coupling network to map current research fronts. Threshold: cosine similarity > 0.1; clustering: Louvain algorithm.
- Co-authorship analysis: author and country collaboration networks to reveal social structure. Threshold: at least 2 co-authored documents; clustering: modularity optimization.
- Structural holes: effective size, constraint, and betweenness centrality to identify brokerage roles.
- Tools: CiteSpace 6.3.R1 (co-citation, coupling), VOSviewer (co-authorship), custom Python (structural holes via NetworkX).

**Feeds results sections:** S2 (intellectual structure), S3 (social structure), S5 (research fronts)

**Scopus search string:** `TITLE-ABS-KEY("co-citation analysis" AND "engineering education" AND "CiteSpace") AND PUBYEAR > 2020`

**Estimated word count:** 200–250 words

---

### 6. Conceptual and Thematic Analysis

**Key points:**
- Keyword co-occurrence: author keywords and Index Keywords; normalization by association strength; clustering via VOSviewer (resolution parameter = 1.0).
- Strategic thematic diagram: Callon centrality and density to classify clusters into motor, basic, niche, and emerging/declining themes.
- Inductive thematic coding: LLM-assisted extraction of latent themes from titles and abstracts (GPT-4, temperature=0.2, top_p=0.9). Unit of analysis: individual article. Coding logic: iterative refinement with human validation (two rounds of 30% random sample checked by domain expert).
- Consensus tier: universal (3/3 model families), majority (≥2/3), idiosyncratic (1/3) — applied to LLM-derived themes.
- Epistemic status: LLM-assisted themes are supportive, not central; all LLM outputs were human-validated before inclusion.

**Feeds results sections:** S4 (conceptual structure), S5 (research fronts), S6 (gaps and future directions)

**Scopus search string:** `TITLE-ABS-KEY("thematic analysis" AND "bibliometric" AND "engineering education" AND "LLM") AND PUBYEAR > 2020`

**Estimated word count:** 200–250 words

---

### 7. Advanced Bibliometric Methods: CiteSpace Spectroscopy and Leiden Indicators

**Key points:**
- CiteSpace burst detection: Kleinberg's algorithm (gamma=1.0, minimum duration=2 years) to identify keyword and reference citation bursts, signaling emerging topics.
- CiteSpace spectral clustering: timeline visualization of co-citation clusters, with sigma metric (betweenness × burst) to highlight pivotal works.
- Leiden indicators: FWCI (field-weighted citation impact), MNCS (mean normalized citation score), PP(top 10%) (proportion of highly cited papers), with bootstrap 95% confidence intervals (1,000 resamples).
- APC analysis: comparison of articles with vs. without author payment charges; Mann-Whitney U test for citation impact differences.

**Feeds results sections:** S5 (research fronts), S7 (impact and quality indicators), S9 (Research Dynamics Manifold)

**Scopus search string:** `TITLE-ABS-KEY("CiteSpace" AND "burst detection" AND "engineering education") AND PUBYEAR > 2020`

**Estimated word count:** 180–220 words

---

### 8. Cross-Phase Triangulation and Convergence Assessment

**Key points:**
- Triangulation design: compare findings from bibliometric (co-citation, coupling, co-authorship), conceptual (keyword co-occurrence, inductive themes), and impact (FWCI, APC) streams.
- Convergence criteria: thematic alignment (e.g., same topic appearing in both co-citation clusters and inductive themes), structural consistency (e.g., collaboration patterns matching citation impact), and divergence identification (e.g., gap between highly cited works and emerging themes).
- Output: a cross-cutting synthesis identifying stable patterns, complementary insights, and contradictory signals across methods.
- This phase directly supports the integrated interpretation in the Discussion.

**Feeds results sections:** S8 (cross-cutting patterns), S9 (Research Dynamics Manifold)

**Scopus search string:** `TITLE-ABS-KEY("triangulation" AND "bibliometric" AND "mixed methods") AND PUBYEAR > 2020`

**Estimated word count:** 100–130 words

---

### Summary Table

| Subsection | Feeds Sections | Estimated Words |
|------------|----------------|-----------------|
| 1. Study Design | S1–S8 | 120–150 |
| 2. Search Strategy | S1, S2 | 180–220 |
| 3. Data Enrichment | S1–S4, S7 | 150–180 |
| 4. Descriptive Bibliometrics | S1, S4 | 130–160 |
| 5. Network Analysis | S2, S3, S5 | 200–250 |
| 6. Conceptual/Thematic Analysis | S4–S6 | 200–250 |
| 7. Advanced Methods | S5, S7, S9 | 180–220 |
| 8. Triangulation | S8, S9 | 100–130 |
| **Total** | | **1,260–1,610** |

*Note: Final word count will be adjusted to 1,000–1,400 by condensing descriptive sections and merging where logical.*

---

*Hallucination control: grounding=0%, flags=0*
