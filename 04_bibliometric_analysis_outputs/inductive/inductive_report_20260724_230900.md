# Inductive Thematic Analysis Report

**Session ID:** 20260724_230900
**Date:** 2026-07-24 23:10
**Total articles:** 96
**Valid abstracts:** 94
**Provider:** Mistral
**Extraction model:** mistral-small-latest
**Reasoning model:** mistral-small-latest
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
| Current provider | Mistral |
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
| Quote Grounding | **87.0%** |
| Article Grounding | **100.0%** |
| Taxonomy Grounding | **100.0%** |
| Theme Reference Grounding | **100.0%** |
| Combined Grounding | **90.9%** |
| Hallucination Flags | 12 |
| Verification Status | review_needed |

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

### Assessment Instrument Development and Validation for Engineering Competencies
- **Studies:** ~46 (soporte real: 46 articulos)
- **Robustness:** High
- **Definition:** The methodological process of creating, validating, and applying instruments (e.g., rubrics, scales, questionnaires) to assess engineering students' technical, professional, and soft skills. This includes expert judgment, psychometric validation, and application in educational contexts.
- **Subthemes:** Rubric-based assessment design and validation, Psychometric instrument development (scales, questionnaires), Competency assessment in engineering education

### Transversal and Employability Skills in Engineering Education
- **Studies:** ~19 (soporte real: 19 articulos)
- **Robustness:** High
- **Definition:** The emphasis on non-technical competencies essential for engineering graduates' professional success, including teamwork, communication, leadership, problem-solving, critical thinking, and innovation. This includes assessment and validation of these skills in educational and workplace contexts.
- **Subthemes:** Teamwork and communication skills, Leadership and innovation competencies, Employability and transferable skills

### Self-Efficacy and Identity Development in Engineering
- **Studies:** ~22 (soporte real: 22 articulos)
- **Robustness:** High
- **Definition:** The study of engineering students' self-efficacy (domain-specific and general) and identity development, and their relationship with academic performance, retention, and professional success. This includes the measurement and validation of instruments assessing these constructs.
- **Subthemes:** Engineering identity development, Domain-specific and general self-efficacy, Relationship with academic and professional outcomes

### Critical Thinking and Advanced Problem-Solving Competencies
- **Studies:** ~9 (soporte real: 9 articulos)
- **Robustness:** High
- **Definition:** The assessment of engineering students' critical thinking, problem-solving, representational competence, and systems thinking abilities. This includes the development and validation of instruments to evaluate these advanced cognitive skills in technical domains.
- **Subthemes:** Critical thinking and problem-solving assessment, Systems thinking and complex problem analysis, Representational competence

### Motivational and Entrepreneurial Mindset in Engineering
- **Studies:** ~10 (soporte real: 10 articulos)
- **Robustness:** High
- **Definition:** The validation and application of instruments to assess engineering students' motivational attitudes, learning strategies, and entrepreneurial mindset. This includes factors such as ambition, innovation, and design thinking capabilities.
- **Subthemes:** Motivation and learning strategies, Entrepreneurial mindset and design thinking, Ambitiousness and innovation factors

### Research Competencies and Academic Skills
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** The assessment of research-related competencies, including intellectual elaboration, technical, and communicative skills, particularly in the context of engineering students' research training and academic writing. This includes the evaluation of scientific literacy and academic performance.
- **Subthemes:** Research training, Academic writing, Scientific literacy

### Resilience and Academic Performance
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The study of resilience as a factor influencing engineering students' academic engagement, performance, and retention. This includes the development and validation of resilience measures and the identification of protective factors that support student success.
- **Subthemes:** Academic resilience, Student retention, Protective factors

### Gender and Diversity in Engineering Education
- **Studies:** ~6 (soporte real: 6 articulos)
- **Robustness:** High
- **Definition:** The examination of gender differences, diversity, and inclusivity in engineering education. This includes the validation of instruments for gender invariance and the assessment of attitudes and experiences related to diversity and inclusivity.
- **Subthemes:** Gender invariance, Diversity, Inclusivity

### Workplace Competency Assessment through Internships
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** The adaptation and validation of instruments to evaluate engineering students' professional development during work-based learning experiences, including internships and apprenticeships. This focuses on measuring workplace competencies, reflective practices, and alignment with industry expectations.
- **Subthemes:** Internship evaluation, Workplace competencies, Apprenticeship assessment

### Real-World and Community-Engaged Learning Assessment
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The evaluation of engineering students' perceptions, self-efficacy, and sense of belonging in community-partnered projects and industry-coupled problem-based learning. This includes measuring outcomes related to social responsibility, teamwork, and contextualized learning.
- **Subthemes:** Community-partnered projects, Real-world learning, Industry-coupled problem-based learning

### Leadership Development and Self-Efficacy in Engineering Education
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The assessment and enhancement of leadership skills and leadership self-efficacy in engineering students through validated instruments and structured programs. This theme emphasizes the measurement of leadership competencies and their relationship with engineering students' professional development and career outcomes.
- **Subthemes:** Leadership self-efficacy measurement, Leadership program evaluation, Domain-specific leadership competencies

### Affective and Writing-Related Factors in Engineering Education
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The study of emotional and attitudinal factors, particularly writing apprehension and attitudes, and their impact on engineering students' academic performance, persistence, and career trajectories. This theme explores how affective dimensions influence learning and professional development.
- **Subthemes:** Writing apprehension and academic success, Emotional factors in engineering learning, Affective factors and career outcomes

### Domain-Specific Self-Efficacy in Biomedical Engineering
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The assessment of self-efficacy in biomedical engineering students and professionals, focusing on clinical problem-solving, grant writing, and interdisciplinary skills. This theme highlights the unique competencies required in biomedical engineering contexts.
- **Subthemes:** Clinical problem-solving self-efficacy, Grant writing self-efficacy, Interdisciplinary skill development

### Structural Signatures (Mejora 5)

| Theme | Source Batches | Articles | Quotes | Combined Grounding |
|-------|--------------|----------|--------|-------------------|
| Assessment Instrument Development and Validation for Engineering Competencies | 4 | 46 | 5 | 90.0% |
| Transversal and Employability Skills in Engineering Education | 3 | 19 | 5 | 90.0% |
| Self-Efficacy and Identity Development in Engineering | 4 | 22 | 5 | 95.0% |
| Critical Thinking and Advanced Problem-Solving Competencies | 3 | 9 | 5 | 90.0% |
| Motivational and Entrepreneurial Mindset in Engineering | 2 | 10 | 5 | 90.0% |
| Research Competencies and Academic Skills | 1 | 3 | 5 | 100.0% |
| Resilience and Academic Performance | 1 | 2 | 5 | 100.0% |
| Gender and Diversity in Engineering Education | 2 | 6 | 5 | 100.0% |
| Workplace Competency Assessment through Internships | 1 | 3 | 5 | 100.0% |
| Real-World and Community-Engaged Learning Assessment | 1 | 2 | 5 | 100.0% |
| Leadership Development and Self-Efficacy in Engineering Education | 1 | 1 | 5 | 90.0% |
| Affective and Writing-Related Factors in Engineering Education | 1 | 1 | 5 | 85.0% |
| Domain-Specific Self-Efficacy in Biomedical Engineering | 1 | 1 | 5 | 90.0% |

---

## Phase 2: Analytical Axes

### Methodological Rigor in Competency Assessment
- **Coverage:** ~50%
- **Justification:** This axis captures the central role of instrument development and validation in assessing engineering competencies, including transversal skills, self-efficacy, and critical thinking.
- **Research potential:** Could inform best practices for designing and validating assessment tools in engineering education, ensuring alignment with industry and academic standards.

### Transversal Skills and Employability
- **Coverage:** ~20%
- **Justification:** Transversal skills (e.g., teamwork, leadership) are frequently assessed in relation to employability, bridging academic and professional contexts.
- **Research potential:** Could guide the integration of transversal skills into curricula and workplace assessments, addressing gaps in current practices.

### Self-Efficacy and Identity Development
- **Coverage:** ~23%
- **Justification:** Self-efficacy and identity are core constructs linked to academic and professional outcomes, often assessed using validated instruments.
- **Research potential:** Could explore interventions to enhance self-efficacy and identity, particularly in underrepresented groups, to improve retention and performance.

### Real-World and Workplace Learning
- **Coverage:** ~5%
- **Justification:** Workplace and community-engaged learning assessments focus on competencies developed in real-world contexts, complementing academic assessments.
- **Research potential:** Could investigate the long-term impact of real-world learning on career readiness and professional development.

### Affective and Domain-Specific Factors
- **Coverage:** ~2%
- **Justification:** Affective factors (e.g., writing apprehension) and domain-specific competencies (e.g., biomedical engineering) are emerging areas with limited but critical studies.
- **Research potential:** Could address gaps in understanding how affective and domain-specific factors influence learning and career outcomes.

---

## Phase 3: Proposed Frameworks

### Framework 1: Instrument-Centric Framework
**Justification:** This framework centers on the dominant theme of assessment instrument development and validation, which underpins most empirical studies in the dataset. It allows for a deep dive into methodological rigor while exploring how instruments are applied across other competency domains.

**General Objective:** To analyze the role of assessment instruments in engineering education, focusing on their development, validation, and application across diverse competency domains.

**Specific Objectives:**
- To examine the methodological processes and psychometric rigor employed in the development and validation of assessment instruments for engineering competencies.
- To investigate how assessment instruments are used to evaluate transversal and employability skills in engineering education.
- To assess the relationship between instrument development practices and the measurement of self-efficacy and identity development in engineering students.
- To explore the application of validated instruments in assessing critical thinking and advanced problem-solving competencies.

**Coverage:** ~60-70%

### Framework 2: Competency-Domain Framework
**Justification:** This framework organizes findings by competency domains, reflecting the empirical distribution of studies across themes. It enables a comparative analysis of how different competencies are assessed and their interrelationships.

**General Objective:** To compare and contrast the assessment, development, and validation of various engineering competencies, emphasizing their interrelationships and methodological approaches.

**Specific Objectives:**
- To analyze the assessment instruments and methodologies used for transversal and employability skills in engineering education.
- To evaluate the role of self-efficacy and identity development in engineering education, including their measurement and impact on outcomes.
- To examine the assessment of critical thinking and advanced problem-solving competencies, including the development of specialized instruments.
- To investigate the relationship between motivational and entrepreneurial mindset and employability skills, including their assessment.

**Coverage:** ~70-80%

### Framework 3: Methodological-Outcome Framework
**Justification:** This framework links methodological rigor (instrument development) with outcomes (e.g., self-efficacy, employability) and contextual factors (e.g., gender, diversity). It reflects the empirical relationships identified in the dataset.

**General Objective:** To explore how methodological rigor in assessment instrument development influences engineering education outcomes and contextual factors.

**Specific Objectives:**
- To assess the methodological rigor of assessment instruments used to evaluate engineering competencies and their alignment with industry and academic standards.
- To investigate the relationship between validated assessment instruments and outcomes such as self-efficacy, identity development, and employability.
- To examine how gender and diversity considerations are integrated into the development and validation of assessment instruments.
- To evaluate the role of real-world and workplace learning assessments in complementing academic assessments of engineering competencies.

**Coverage:** ~60-70%

---

## Recommendation

Competency-Domain Framework This framework provides the most comprehensive coverage of the dataset (~70-80%) while enabling comparative analysis across all major themes. It aligns well with the empirical distribution of studies and allows for a balanced exploration of both methodological and thematic dimensions. The framework also highlights gaps and overlaps in assessment practices, which can guide future research and policy.

---

## Traceability

This analysis is fully traceable. See:
- Results: `inductive_results_20260724_230900.json`
- Trace log: `logs/trace_20260724_230900.json`
- Cache: `.cache/20260724_230900_*`
- CSV exports: `csv/`