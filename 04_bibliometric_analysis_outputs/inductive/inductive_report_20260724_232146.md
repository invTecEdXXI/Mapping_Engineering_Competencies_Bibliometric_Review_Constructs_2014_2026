# Inductive Thematic Analysis Report

**Session ID:** 20260724_232146
**Date:** 2026-07-24 23:30
**Total articles:** 96
**Valid abstracts:** 94
**Provider:** DeepSeek
**Extraction model:** deepseek-v4-pro
**Reasoning model:** deepseek-v4-pro
**Experiment mode:** same_model_all_phases

> **Scope declaration:** this analysis is based exclusively on **title + abstract**
> text of each included record — no full-text (PDF) content was read or analyzed.
> Evidence quotes are verified (grounding score) against the abstract field only;
> see `prompts/inductive/phase1_extract_v1.txt` for the exact extraction instructions.

---

## Methodology

This analysis used an **inductive approach** where themes emerged from the data
without predefined categories. The analysis followed three phases:

1. **Phase 1:** Inductive thematic mapping (batch processing)
2. **Phase 2:** Cross-thematic analysis (relationships)
3. **Phase 3:** Analytical framework construction

### Experiment Configuration

| Parameter | Value |
|-----------|-------|
| Batching policy | sequential |
| Batch seed | None |
| Batch size | None |
| Temperature | 0.3 |
| Prompt version | v1 |
| Schema version | v1 |

### Provider Capability (Mejora 7)

| Property | Value |
|----------|-------|
| Interface | openai_compat |
| Current provider | DeepSeek |
| Protocol invariance tested | False |

### Prompt Hashes (Mejora 3)

| Prompt/Schema | Hash |
|---------------|------|
| prompt:phase1_extract | `6cf44d6b1e52b430` |
| prompt:phase1_synthesis | `14048a944e650cd5` |
| prompt:phase2_cross | `1f69a490f8847874` |
| prompt:phase3_framework | `c556b142f4e0ed71` |
| schema:phase1_output | `d9250e855d06c8f7` |
| schema:phase2_output | `7c26ff66f527bba8` |
| schema:phase3_output | `60ffa3d3f93aaacb` |

### Hallucination Control — Separated Metrics (Mejora 9)

| Metric | Value |
|--------|-------|
| Quote Grounding | **100.0%** |
| Article Grounding | **100.0%** |
| Taxonomy Grounding | **100.0%** |
| Theme Reference Grounding | **95.9%** |
| Combined Grounding | **100.0%** |
| Hallucination Flags | 0 |
| Verification Status | verified |

### Batching Details (Mejora 2)

- **Strategy:** sequential
- **Seed:** None
- **N batches:** 4

| Batch | N articles |
|-------|-----------|
| 0 | 30 |
| 1 | 30 |
| 2 | 30 |
| 3 | 4 |

---

## Phase 1: Emergent Taxonomy

### Scale Development and Psychometric Evaluation
- **Studies:** ~12 (soporte real: 12 articulos)
- **Robustness:** Medium
- **Definition:** The systematic design, refinement, and empirical testing of measurement instruments through item generation, factor analysis to identify latent dimensions, and the accumulation of reliability and validity evidence to support meaningful and consistent interpretation of scores.
- **Subthemes:** Item Generation and Scale Construction, Factor Structure Investigation (EFA/CFA), Reliability and Validity Evidence

### Self-Efficacy Measurement
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** The assessment of individuals' beliefs in their capabilities to perform specific tasks or achieve desired outcomes, with applications across leadership, entrepreneurship, and clini
- **Subthemes:** General self-efficacy, Domain-specific self-efficacy, Self-efficacy and performance, Mediation effects

### Motivation and Affective Constructs in Engineering Students
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The study of psychological drivers such as motivation, attitudes, emotions, and writing apprehension that influence engineering students' engagement with entrepreneurial careers, a
- **Subthemes:** Entrepreneurial motivation, Writing attitudes, Affect and emotion, Writer's block

### Engineering Education Context
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** Medium
- **Definition:** All studies are situated within engineering education, focusing on the development, assessment, and professional readiness of undergraduate or graduate engineering students, often 
- **Subthemes:** Accreditation requirements, Curriculum design, Skill development, Engineering identity

### Career and Professional Development
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** Medium
- **Definition:** The instruments and constructs are explicitly linked to students' career intentions, professional trajectories, persistence, and success in engineering, including entrepreneurial v
- **Subthemes:** Entrepreneurial intention, Graduate persistence, Leadership development, Grant writing skills

### Structural Signatures (Mejora 5)

| Theme | Source Batches | Articles | Quotes | Combined Grounding |
|-------|--------------|----------|--------|-------------------|
| Scale Development and Psychometric Evaluation | 1 | 12 | 5 | 90.0% |
| Self-Efficacy Measurement | 1 | 3 | 5 | 100.0% |
| Motivation and Affective Constructs in Engineering Students | 1 | 2 | 5 | 100.0% |
| Engineering Education Context | 1 | 4 | 5 | 100.0% |
| Career and Professional Development | 1 | 4 | 5 | 100.0% |

---

## Phase 2: Analytical Axes

### Psychometric Instrumentation for Engineering Education Outcomes
- **Coverage:** ~20% of studies
- **Justification:** A central focus is the creation and validation of scales tailored to engineering students' self-efficacy, motivation, and career readiness, reflecting the need for context-specific measurement tools.
- **Research potential:** Enables systematic benchmarking of affective and professional competencies across engineering programs, supporting evidence-based curriculum design and accreditation compliance.

### Affective and Cognitive Pathways to Professional Development
- **Coverage:** ~15% of studies
- **Justification:** Studies intertwine self-efficacy, motivation, and emotions to explain career intentions and persistence, highlighting mediation and direct effects.
- **Research potential:** Informs interventions targeting specific psychological drivers (e.g., entrepreneurial self-efficacy) to boost retention and transition into engineering careers.

### Contextualizing Scale Validation within Accreditation and Skill Frameworks
- **Coverage:** ~10% of studies
- **Justification:** The engineering education setting imposes unique accreditation requirements and skill development goals, making instrument validation a means to demonstrate program effectiveness.
- **Research potential:** Provides a framework for aligning psychometric evidence with ABET outcomes, improving accountability and graduate preparedness.

---

## Phase 3: Proposed Frameworks

### Framework 1: Methodological and Instrumentation Trajectory
**Justification:** The data reveal a clear progression from scale development and validation to the application of instruments in measuring self-efficacy, motivation, and career outcomes within engineering education; this framework organizes studies along this continuum to highlight gaps and best practices.

**General Objective:** To track the methodological lifecycle of psychometric instruments, from initial development through validation to application, in assessing engineering students' psychological and professional attributes.

**Specific Objectives:**
- Examine scale development and psychometric evaluation processes, including item generation, factor analysis, and reliability/validity evidence across studies.
- Investigate the measurement of self-efficacy and motivational constructs using validated instruments in engineering education contexts.
- Assess how psychometrically sound instruments predict career intentions and professional development outcomes, linking measurement to real-world engineering trajectories.
- Evaluate the role of the engineering education context in shaping instrument focus and validation criteria, including accreditation and curriculum alignment.

**Coverage:** 60-70%

### Framework 2: Construct Interplay and Mediation Pathways
**Justification:** The relationships among self-efficacy, motivation, and career outcomes form a network of direct and mediated effects; this framework organizes findings to map these pathways and identify key drivers of professional development in engineering students.

**General Objective:** To delineate the interrelationships among self-efficacy, motivational/affective constructs, and career-related outcomes, focusing on mediation and direct effects that explain engineering students' professional intentions and skills.

**Specific Objectives:**
- Synthesize evidence on the measurement and role of self-efficacy, both general and domain-specific, in engineering student populations.
- Analyze the influence of motivation and affective constructs (e.g., entrepreneurial motivation, writing attitudes) on self-efficacy and career intentions.
- Examine the direct and mediated pathways from psychological constructs to career and professional development outcomes, such as entrepreneurial intention and persistence.
- Identify contextual factors within engineering education that moderate or influence these construct relationships.

**Coverage:** 50-60%

### Framework 3: Educational and Professional Outcome Assessment
**Justification:** Many studies ultimately aim to assess career readiness, entrepreneurial intention, and skill acquisition in engineering students, using validated instruments as tools; this framework centers on these outcomes and how they are measured and predicted.

**General Objective:** To consolidate findings on the assessment of engineering students' professional outcomes—including career intentions, leadership, and writing skills—through psychometrically validated instruments, and to determine the predictive value of psychological constructs.

**Specific Objectives:**
- Catalog the psychometric instruments used to assess career-related outcomes in engineering education, including their validation status.
- Investigate how self-efficacy beliefs (general and domain-specific) predict entrepreneurial intentions, graduate persistence, and leadership development.
- Assess the role of motivation and affective factors (e.g., entrepreneurial motivation, writing attitudes) in developing writing skills and entrepreneurial intentions.
- Evaluate how the engineering education context (accreditation, curriculum) shapes the measurement and importance of these professional outcomes.

**Coverage:** 70-80%

---

## Recommendation

Framework 3, 'Educational and Professional Outcome Assessment', because it aligns with the practical need for evidence-based evaluation in engineering education, has the highest estimated coverage, and bridges psychometric rigor with career readiness objectives. It also leverages the strongest themes (Scale Development and Career) and their relationships, making the review more actionable for educators and policymakers.

---

## Traceability

This analysis is fully traceable. See:
- Results: `inductive_results_20260724_232146.json`
- Trace log: `logs/trace_20260724_232146.json`
- Cache: `.cache/20260724_232146_*`
- CSV exports: `csv/`