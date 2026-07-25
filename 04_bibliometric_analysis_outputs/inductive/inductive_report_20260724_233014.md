# Inductive Thematic Analysis Report

**Session ID:** 20260724_233014
**Date:** 2026-07-24 23:35
**Total articles:** 96
**Valid abstracts:** 94
**Provider:** Mistral
**Extraction model:** mistral-large-latest
**Reasoning model:** mistral-large-latest
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
| Quote Grounding | **83.3%** |
| Article Grounding | **100.0%** |
| Taxonomy Grounding | **100.0%** |
| Theme Reference Grounding | **100.0%** |
| Combined Grounding | **88.3%** |
| Hallucination Flags | 17 |
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

### Transversal and Professional Competencies in Engineering Education
- **Studies:** ~25 (soporte real: 25 articulos)
- **Robustness:** High
- **Definition:** The assessment and development of non-technical, transferable, and sociotechnical competencies essential for professional success in engineering. This includes skills such as communication, teamwork, leadership, problem-solving, lifelong learning, entrepreneurial skills, and understanding the social implications of technology.
- **Subthemes:** Generic and professional competencies (e.g., communication, teamwork, leadership), Transversal competencies (e.g., lifelong learning, entrepreneurial skills), Sociotechnical competencies (e.g., understanding social implications of technology)

### Self-Efficacy, Attitudes, and Engineering Identity
- **Studies:** ~59 (soporte real: 59 articulos)
- **Robustness:** High
- **Definition:** The development, validation, and exploration of instruments and factors related to engineering students' self-efficacy, attitudes, and identity. This includes measuring confidence in performing specific tasks, understanding predictors of engineering identity (e.g., self-efficacy, recognition, interest), and examining how these constructs influence students' experiences and outcomes in engineering education.
- **Subthemes:** Self-efficacy and attitudinal measurement in engineering contexts, Factors contributing to engineering identity (e.g., self-efficacy, recognition, interest)

### Critical Thinking, Problem-Solving, Creativity, and Design Mindset in Engineering
- **Studies:** ~11 (soporte real: 11 articulos)
- **Robustness:** High
- **Definition:** The development and validation of instruments to assess critical thinking, problem-solving, creativity, design thinking, and related constructs in engineering students. This includes domain-specific and general approaches to evaluating these competencies, as well as their role in fostering innovation and effective engineering practice.
- **Subthemes:** Critical thinking and problem-solving skills in engineering, Creativity, design thinking, and innovation in engineering education

### Psychometric and Analytical Methods in Engineering Education Research
- **Studies:** ~23 (soporte real: 23 articulos)
- **Robustness:** High
- **Definition:** The evaluation of the reliability, validity, and structural properties of assessment instruments in engineering education, alongside the application of analytical methods (e.g., mediation and correlation analyses) to explore relationships between constructs. This includes factor analysis, confirmatory factor analysis, and statistical modeling to understand how variables such as self-efficacy, motivation, and competencies interact.
- **Subthemes:** Psychometric evaluation of engineering assessment instruments, Mediation and correlation analysis in engineering education research

### Rubric-Based Competency Assessment in Engineering
- **Studies:** ~21 (soporte real: 21 articulos)
- **Robustness:** High
- **Definition:** The use of rubrics as structured assessment tools to evaluate specific competencies in engineering students, particularly in laboratory, project-based, or practical settings. Emphasis is placed on expert judgment, inter-rater reliability, and performance assessment.
- **Subthemes:** Expert judgment, Inter-rater reliability, Performance assessment

### Research Competencies and Investigative Skills in Engineering Students
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** The assessment and development of research-related competencies in engineering students, including intellectual, technical, and communicative skills necessary for conducting and presenting research. This encompasses research training, scientific writing, and data collection techniques.
- **Subthemes:** Research training, Scientific writing, Data collection techniques

### Motivation and Learning Strategies in Engineering Education
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** The assessment of students' motivational attitudes, behaviors, and strategies for learning in engineering contexts, including intrinsic and extrinsic motivation, self-regulated learning, and expectancy-value frameworks. This theme emphasizes the development and validation of instruments to measure these constructs and their impact on academic performance and persistence.
- **Subthemes:** Intrinsic and extrinsic motivation, Self-regulated learning strategies, Expectancy-value theory in engineering

### Assessment of Professional Ethics and Social Responsibility in Engineering
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** The development and validation of tools to measure engineering students' professional ethics, social responsibility, and sustainability attitudes. This theme includes the assessment of students' awareness of ethical dilemmas, social implications of engineering, and commitment to responsible practice.
- **Subthemes:** Ethics education and assessment, Social responsibility in engineering, Sustainability attitudes

### Community-Partnered and Experiential Learning in Engineering
- **Studies:** ~9 (soporte real: 9 articulos)
- **Robustness:** High
- **Definition:** The use of real-world, community-based projects, internships, or problem-based learning to enhance engineering students' professional skills, sense of belonging, and practical competencies. This theme includes the assessment of learning outcomes from experiential and collaborative educational approaches.
- **Subthemes:** Problem-based learning outcomes, Internship and workplace experience, Community-engaged engineering projects

### Cultural and Linguistic Adaptation of Engineering Assessment Tools
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** The process of translating, adapting, and validating assessment instruments for use in diverse cultural or linguistic settings. This theme includes ensuring measurement invariance, cross-cultural validity, and linguistic equivalence to maintain the reliability and validity of engineering education assessments.
- **Subthemes:** Cross-cultural validation of instruments, Measurement invariance testing, Linguistic adaptation of assessments

### Gender Differences in Engineering Competencies and Self-Efficacy
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** Medium
- **Definition:** The examination of how gender influences engineering students' self-efficacy, competencies, and experiences, including the identification of gaps, gendered experiences, and the development of strategies to address disparities through curricular interventions.
- **Subthemes:** Gendered experiences in engineering education, Self-efficacy gaps between genders, Curricular interventions to reduce gender disparities

### Innovation and Entrepreneurship Competencies in Engineering
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** High
- **Definition:** The assessment and development of competencies related to innovation, entrepreneurship, and the ability to create or adapt to new technologies and business models in engineering students. This includes the measurement of innovation self-efficacy and entrepreneurial competencies.
- **Subthemes:** Innovation self-efficacy, Entrepreneurial competencies, Career aspirations in engineering innovation

### Affective Dimensions of Writing in Engineering Education
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The exploration of engineering students' attitudes, emotions, and perceptions toward academic writing, including the development of tools to assess writing apprehension, writing attitudes, and their impact on career trajectory and graduate student persistence.
- **Subthemes:** Writing attitudes survey, Writing apprehension, Career trajectory impact, Graduate student persistence

### Structural Signatures (Mejora 5)

| Theme | Source Batches | Articles | Quotes | Combined Grounding |
|-------|--------------|----------|--------|-------------------|
| Transversal and Professional Competencies in Engineering Education | 4 | 25 | 5 | 85.0% |
| Self-Efficacy, Attitudes, and Engineering Identity | 4 | 59 | 5 | 85.0% |
| Critical Thinking, Problem-Solving, Creativity, and Design Mindset in Engineering | 3 | 11 | 5 | 85.0% |
| Psychometric and Analytical Methods in Engineering Education Research | 2 | 23 | 5 | 85.0% |
| Rubric-Based Competency Assessment in Engineering | 2 | 21 | 5 | 100.0% |
| Research Competencies and Investigative Skills in Engineering Students | 1 | 3 | 5 | 100.0% |
| Motivation and Learning Strategies in Engineering Education | 1 | 3 | 5 | 100.0% |
| Assessment of Professional Ethics and Social Responsibility in Engineering | 1 | 3 | 5 | 100.0% |
| Community-Partnered and Experiential Learning in Engineering | 2 | 9 | 5 | 95.0% |
| Cultural and Linguistic Adaptation of Engineering Assessment Tools | 1 | 3 | 5 | 100.0% |
| Gender Differences in Engineering Competencies and Self-Efficacy | 1 | 4 | 5 | 90.0% |
| Innovation and Entrepreneurship Competencies in Engineering | 2 | 3 | 5 | 95.0% |
| Affective Dimensions of Writing in Engineering Education | 1 | 1 | 5 | 100.0% |

---

## Phase 2: Analytical Axes

---

## Phase 3: Proposed Frameworks

### Framework 1: Competency-Centric Framework
**Justification:** This framework reflects the dominant focus in the data on assessing and developing various competencies in engineering education, both technical and non-technical. It organizes findings around the types of competencies and their assessment methods, which are central to the majority of studies.

**General Objective:** To synthesize and compare approaches for assessing and developing key competencies in engineering education, with a focus on their measurement, validation, and impact on student outcomes.

**Specific Objectives:**
- Examine the assessment and development of transversal, professional, and sociotechnical competencies in engineering education, including their measurement tools and pedagogical strategies.
- Analyze the role of rubric-based and performance assessments in evaluating engineering competencies, with attention to expert judgment and inter-rater reliability.
- Investigate the development and assessment of critical thinking, problem-solving, creativity, and design mindset in engineering students, including domain-specific and general approaches.
- Explore the assessment and cultivation of research competencies and investigative skills in engineering students, focusing on tools and methods for evaluation.

**Coverage:** 70-80%

### Framework 2: Psychosocial and Competency Integration Framework
**Justification:** This framework integrates the two largest thematic clusters in the data: psychosocial constructs (e.g., self-efficacy, identity) and competencies. It reflects the interconnectedness of these themes in the literature, where affective factors often mediate or predict competency development.

**General Objective:** To explore the interplay between psychosocial constructs (e.g., self-efficacy, attitudes, identity) and competency development in engineering education, and how these relationships are measured and analyzed.

**Specific Objectives:**
- Synthesize findings on the development, validation, and role of self-efficacy, attitudes, and engineering identity in shaping student outcomes and experiences.
- Compare psychometric and analytical methods used to evaluate the reliability, validity, and structural properties of instruments assessing psychosocial and competency-related constructs in engineering education.
- Examine how transversal, professional, and sociotechnical competencies are influenced by or interact with psychosocial constructs such as self-efficacy and engineering identity.
- Investigate the role of motivation and learning strategies in the development of engineering competencies and identity, including their assessment and impact.

**Coverage:** 85-95%

### Framework 3: Assessment Methodology Framework
**Justification:** This framework organizes findings around the methodologies used to assess engineering competencies and related constructs. It reflects the data's strong emphasis on psychometric evaluation, rubric-based assessment, and analytical methods, providing a lens to compare the strengths and limitations of different approaches.

**General Objective:** To evaluate and compare the methodologies used to assess competencies, psychosocial constructs, and other key outcomes in engineering education, with a focus on their reliability, validity, and applicability.

**Specific Objectives:**
- Compare the psychometric properties (e.g., reliability, validity) of instruments used to assess self-efficacy, attitudes, engineering identity, and related psychosocial constructs.
- Analyze the use of rubric-based assessments in engineering education, including their design, inter-rater reliability, and effectiveness in evaluating competencies in practical or project-based settings.
- Examine the application of analytical methods (e.g., mediation, correlation, factor analysis) in engineering education research to explore relationships between competencies, psychosocial constructs, and student outcomes.
- Evaluate the tools and approaches used to assess critical thinking, problem-solving, creativity, and design mindset in engineering students, including their domain-specific and general applications.

**Coverage:** 60-70%

---

## Recommendation

Psychosocial and Competency Integration Framework This framework is recommended because it captures the largest proportion of studies (85-95%) and reflects the most robust and interconnected themes in the data. It allows for both descriptive and relational analysis, enabling a comprehensive understanding of how psychosocial constructs (e.g., self-efficacy, identity) interact with competency development. This integrative approach aligns with the empirical patterns observed, where affective and cognitive dimensions are often studied in tandem. Additionally, it provides flexibility for comparative analysis across themes, making it the most versatile and data-driven choice.

---

## Traceability

This analysis is fully traceable. See:
- Results: `inductive_results_20260724_233014.json`
- Trace log: `logs/trace_20260724_233014.json`
- Cache: `.cache/20260724_233014_*`
- CSV exports: `csv/`