# Inductive Thematic Analysis Report

**Session ID:** 20260724_223030
**Date:** 2026-07-24 22:32
**Total articles:** 96
**Valid abstracts:** 94
**Provider:** DeepSeek
**Extraction model:** deepseek-v4-flash
**Reasoning model:** deepseek-v4-flash
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
| Quote Grounding | **92.7%** |
| Article Grounding | **99.7%** |
| Taxonomy Grounding | **100.0%** |
| Theme Reference Grounding | **100.0%** |
| Combined Grounding | **94.8%** |
| Hallucination Flags | 5 |
| Verification Status | warnings |

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

### Instrument Development, Validation, and Psychometric Analysis
- **Studies:** ~91 (soporte real: 91 articulos)
- **Robustness:** High
- **Definition:** The creation, adaptation, and psychometric testing of assessment tools (scales, rubrics, questionnaires) to measure competencies, attitudes, and skills in engineering education. This includes statistical techniques such as exploratory and confirmatory factor analysis, reliability coefficients, and validity measures to ensure robust measurement.
- **Subthemes:** Scale development and refinement, Psychometric properties and factor analysis, Competency assessment tool validation

### Self-Efficacy, Attitudes, and Demographic Influences
- **Studies:** ~42 (soporte real: 42 articulos)
- **Robustness:** High
- **Definition:** Assessment of students' self-perceived confidence, attitudes, and beliefs regarding their abilities, including sources of self-efficacy (e.g., performance accomplishments, vicarious learning). Also examines how demographic factors such as gender, class level, and first-generation status, as well as contextual events like the COVID-19 pandemic, influence self-efficacy and learning outcomes.
- **Subthemes:** Self-efficacy and attitudes measurement, Sources of self-efficacy, Gender and demographic differences, Impact of COVID-19 on self-efficacy

### Specialized Competency and Mindset Assessment
- **Studies:** ~31 (soporte real: 31 articulos)
- **Robustness:** High
- **Definition:** Development and validation of instruments to assess specific competencies and mindsets in engineering education, including transversal and professional skills (e.g., communication, teamwork), entrepreneurial and design mindsets, grit, engineering mindset, foundational mathematics and engineering competences, and global communication competency.
- **Subthemes:** Transversal and professional skills, Entrepreneurial and design mindset, Grit and engineering mindset, Mathematics and engineering fundamentals, Global communication competency

### Identity, Motivation, and Persistence in Engineering
- **Studies:** ~10 (soporte real: 10 articulos)
- **Robustness:** High
- **Definition:** Exploration of how engineering students develop a sense of identity as engineers and how this relates to persistence and intention to complete their studies. Also includes measurement of intrinsic motivation based on Self-Determination Theory and interventions to enhance motivation.
- **Subthemes:** Engineering identity and persistence, Intrinsic motivation and its measurement

### Reflective Thinking and Decision-Making
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The assessment of students' reflective thinking processes and decision-making competencies, particularly in design problem-solving and self-regulated learning contexts.
- **Subthemes:** Reflective thinking, Decision-making, Self-regulated learning, Design problem-solving

### Internship and Work Experience Evaluation
- **Studies:** ~6 (soporte real: 6 articulos)
- **Robustness:** High
- **Definition:** Studies that adapt or validate questionnaires to assess engineering students' perceptions of their internship or work experiences, focusing on factors like workplace support, university support, and the development of generic competencies.
- **Subthemes:** Work Experience Questionnaire (WEQ), Internship experience, Workplace support, Generic competencies

### Structural Signatures (Mejora 5)

| Theme | Source Batches | Articles | Quotes | Combined Grounding |
|-------|--------------|----------|--------|-------------------|
| Instrument Development, Validation, and Psychometric Analysis | 4 | 91 | 5 | 90.0% |
| Self-Efficacy, Attitudes, and Demographic Influences | 4 | 42 | 5 | 92.5% |
| Specialized Competency and Mindset Assessment | 4 | 31 | 5 | 91.0% |
| Identity, Motivation, and Persistence in Engineering | 2 | 10 | 5 | 100.0% |
| Reflective Thinking and Decision-Making | 1 | 2 | 5 | 100.0% |
| Internship and Work Experience Evaluation | 2 | 6 | 5 | 100.0% |

---

## Phase 2: Analytical Axes

### Measurement focus vs. psychological constructs
- **Coverage:** 95%
- **Justification:** Separates studies primarily concerned with instrument development from those focusing on psychological constructs like self-efficacy, identity, and motivation.
- **Research potential:** Helps identify whether research objectives prioritize tool creation or understanding underlying mechanisms.

### Individual vs. contextual factors
- **Coverage:** 80%
- **Justification:** Distinguishes studies focusing on internal attributes (e.g., self-efficacy, identity) from those examining external influences (e.g., internships, demographics, COVID-19).
- **Research potential:** Reveals gaps in integrating individual and contextual factors, informing holistic interventions.

### Competency breadth vs. depth
- **Coverage:** 60%
- **Justification:** Differentiates studies on broad transversal skills from those on specialized competencies (e.g., entrepreneurial mindset, mathematics fundamentals).
- **Research potential:** Highlights the need for balanced assessment frameworks covering both general and specific skills.

---

## Phase 3: Proposed Frameworks

### Framework 1: Psychometric and Construct Coverage Framework
**Justification:** This framework organizes findings by distinguishing between studies focused on instrument development and those examining psychological constructs, reflecting the dominant analytical axis of measurement focus vs. psychological constructs.

**General Objective:** To systematically analyze the distribution and integration of psychometric instrument development and psychological construct assessment in engineering education research.

**Specific Objectives:**
- Evaluate the scope and robustness of instrument development and validation methods across major competency and psychological construct domains.
- Compare the prevalence and measurement approaches for self-efficacy, attitudes, and demographic influences versus identity, motivation, and persistence.
- Assess the integration of reflective thinking and decision-making constructs within broader psychometric frameworks.
- Examine how internship and work experience evaluation instruments complement psychological construct assessments.

**Coverage:** 95%

### Framework 2: Individual-Contextual and Competency Depth Framework
**Justification:** This framework leverages the individual vs. contextual factors and competency breadth vs. depth axes to organize studies by internal attributes, external influences, and competency specificity.

**General Objective:** To investigate how individual psychological attributes and contextual factors interact across broad and specialized competency assessments in engineering education.

**Specific Objectives:**
- Analyze the relationship between self-efficacy, attitudes, and demographic influences (individual factors) and identity, motivation, and persistence.
- Compare the assessment of broad transversal skills versus specialized competencies and mindsets, including their psychometric foundations.
- Evaluate the role of contextual factors (internships, work experience, COVID-19) in shaping self-efficacy and competency development.
- Examine how reflective thinking and decision-making competencies are assessed in relation to individual and contextual factors.

**Coverage:** 80%

### Framework 3: Competency Domain and Psychometric Integration Framework
**Justification:** This framework organizes findings by competency domains (psychological constructs, specialized skills, reflective processes) and their psychometric underpinnings, emphasizing the strong associations between instrument development and construct assessment.

**General Objective:** To synthesize the psychometric validation of competency assessments across psychological, specialized, and reflective domains in engineering education.

**Specific Objectives:**
- Map the psychometric properties and validation methods used for self-efficacy, attitudes, and demographic influence instruments.
- Assess the psychometric quality and domain coverage of specialized competency and mindset assessment tools.
- Investigate the psychometric integration of identity, motivation, and persistence measures with competency assessments.
- Evaluate the psychometric foundations of reflective thinking and decision-making instruments in engineering contexts.

**Coverage:** 90%

---

## Recommendation

I recommend the Psychometric and Construct Coverage Framework because it provides the highest coverage (95%) of the data, directly aligns with the dominant analytical axis (measurement focus vs. psychological constructs), and leverages the strongest empirical relationships (e.g., instrument development with self-efficacy and specialized competencies). It also allows for comparative and relational analyses across all major themes, including the smaller but relevant internship and reflective thinking areas, while maintaining a clear organizational logic grounded in the inductive findings.

---

## Traceability

This analysis is fully traceable. See:
- Results: `inductive_results_20260724_223030.json`
- Trace log: `logs/trace_20260724_223030.json`
- Cache: `.cache/20260724_223030_*`
- CSV exports: `csv/`