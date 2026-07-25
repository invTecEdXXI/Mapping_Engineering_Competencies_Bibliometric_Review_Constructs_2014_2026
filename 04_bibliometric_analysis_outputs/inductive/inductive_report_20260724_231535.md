# Inductive Thematic Analysis Report

**Session ID:** 20260724_231535
**Date:** 2026-07-24 23:17
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
| Quote Grounding | **85.0%** |
| Article Grounding | **100.0%** |
| Taxonomy Grounding | **100.0%** |
| Theme Reference Grounding | **100.0%** |
| Combined Grounding | **89.5%** |
| Hallucination Flags | 14 |
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

### Engineering Competencies, Attitudes, and Professional Skills Assessment
- **Studies:** ~67 (soporte real: 67 articulos)
- **Robustness:** High
- **Definition:** The identification, assessment, and development of both technical and non-technical competencies, attitudes, and professional skills required for engineering students. This includes evaluating constructs such as self-efficacy, teamwork, communication, innovation mindset, and entrepreneurial intentions.
- **Subthemes:** Technical and non-technical competencies, Self-efficacy and attitudinal development, Professional skills (e.g., teamwork, communication), Innovation and entrepreneurial mindset

### Advanced Cognitive and Systems Thinking Skills Assessment
- **Studies:** ~9 (soporte real: 9 articulos)
- **Robustness:** High
- **Definition:** The assessment of higher-order cognitive abilities and systems thinking in engineering contexts. This includes evaluating critical thinking, problem-solving, representational competence, and the ability to think holistically about complex systems and iterative design processes.
- **Subthemes:** Higher-order cognitive skills (e.g., critical thinking, problem-solving), Systems thinking and design mindset, Representational competence

### Innovation, Entrepreneurship, and Career Intentions Assessment
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** High
- **Definition:** The development and assessment of skills and motivations related to innovation, entrepreneurship, and career intentions in engineering students. This includes examining constructs like entrepreneurial mindset, career trajectories, and motivational factors influencing entrepreneurial intentions.
- **Subthemes:** Innovation and entrepreneurial mindset, Entrepreneurial motivation and career intentions

### Experiential and Active Learning Assessment
- **Studies:** ~5 (soporte real: 5 articulos)
- **Robustness:** Medium
- **Definition:** The evaluation of students' competencies, learning gains, and outcomes gained through experiential and active learning strategies. This includes assessing workplace experiences (e.g., internships), flipped classrooms, problem-based learning, and perceived learning gains.
- **Subthemes:** Workplace and experiential learning assessment, Active learning strategies and learning gains

### Sustainability, Ethics, and Leadership Competencies Assessment
- **Studies:** ~5 (soporte real: 5 articulos)
- **Robustness:** High
- **Definition:** The measurement of students' competencies, attitudes, and values related to sustainability, social responsibility, ethics, and leadership in engineering practice. This includes frameworks for assessing ethical decision-making, team motivation, and innovative change management.
- **Subthemes:** Sustainability and social responsibility, Ethics in engineering practice, Leadership competencies

### Assessment Instrument Development and Validation
- **Studies:** ~54 (soporte real: 54 articulos)
- **Robustness:** High
- **Definition:** The process of creating, refining, and validating tools (e.g., scales, rubrics, questionnaires) to measure engineering students' competencies, attitudes, or skills. This includes psychometric testing such as reliability (Cronbach's alpha, McDonald's omega) and validity (construct, content, discriminant) analyses.

### Educational Contexts and Assessment Environments
- **Studies:** ~23 (soporte real: 23 articulos)
- **Robustness:** Medium
- **Definition:** The diverse settings and contexts in which engineering students are assessed, including traditional classrooms, laboratories, internships, virtual learning environments, and graduate programs. This theme captures how different educational contexts influence assessment methods and outcomes.
- **Subthemes:** Laboratory-based assessment, Internship and workplace assessment, Virtual and remote learning assessment, Graduate-level assessment

### Reflective Practices and Metacognition in Engineering Education
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The development and validation of tools to assess students' reflective thinking, particularly in design problem-solving and experiential learning contexts. This theme examines how reflection and metacognition contribute to learning and professional growth.
- **Subthemes:** Reflective practice in design, Timing and objects of reflection, Levels of reflective thinking, Self-reporting instruments for reflection

### Diversity and Inclusion in Engineering Assessment
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** Medium
- **Definition:** The examination of how cultural background, gender, and other demographic factors influence students' competencies, attitudes, and assessment outcomes in engineering education. This theme includes the study of measurement invariance and culturally adapted assessment tools.
- **Subthemes:** Gender invariance in assessment, Cultural adaptation of instruments, Demographic factors in performance, Equity in assessment outcomes

### Mathematical and Technical Competency Assessment
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The assessment of foundational mathematical and technical competencies in engineering students, particularly at the beginning of their academic journey. This includes the use of psychometric tools like Rasch analysis to evaluate skills in real-world applications.
- **Subthemes:** Mathematical competence, Technical skills, Psychometric evaluation

### Large-Scale and Cross-Cultural Competency Benchmarking
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** The design, implementation, and analysis of large-scale assessments of engineering competencies, often involving international collaborations, multi-institutional participation, or cross-cultural validation to benchmark student performance and inform curriculum improvements.
- **Subthemes:** International benchmarking frameworks, Vocational competencies in global contexts, Cross-cultural validation of assessment tools

### Pedagogical Interventions and Learning Outcomes Assessment
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** The development and evaluation of pedagogical strategies, curricular changes, or interventions (e.g., flipped classrooms, problem-based learning) aimed at enhancing engineering students' competencies, assessed through pre- and post-intervention measures of learning gains and skill development.
- **Subthemes:** Active learning strategy evaluation, Interdisciplinary project-based learning, Curriculum alignment with competency outcomes

### Writing Attitudes and Academic Performance in Engineering
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The evaluation of engineering students' attitudes toward writing, including emotional responses (e.g., apprehension) and cognitive engagement, and their relationship to academic success and career development. This theme also encompasses the validation of survey instruments used to measure these attitudes.
- **Subthemes:** Writing apprehension and performance, Survey validation methodologies, Career trajectory implications

### Self-Efficacy in Biomedical Engineering Contexts
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The measurement of self-efficacy among biomedical engineering students, particularly their confidence in addressing clinical problems, proposing solutions, and engaging in interdisciplinary collaborations. This theme emphasizes the clinical relevance of self-efficacy and its role in professional development.
- **Subthemes:** Clinical problem-solving self-efficacy, Interdisciplinary skill confidence, Grant proposal writing efficacy

### Educational Assessment Policy and Institutional Impact
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The use of validated assessment instruments to inform institutional policies, educational research, and broader policy decisions in engineering education. This theme explores how assessment outcomes drive curriculum development, accreditation processes, and systemic improvements in engineering programs.
- **Subthemes:** Institutional assessment frameworks, Policy development from assessment data, Educational outcomes and accreditation

### Structural Signatures (Mejora 5)

| Theme | Source Batches | Articles | Quotes | Combined Grounding |
|-------|--------------|----------|--------|-------------------|
| Engineering Competencies, Attitudes, and Professional Skills Assessment | 4 | 67 | 5 | 92.5% |
| Advanced Cognitive and Systems Thinking Skills Assessment | 3 | 9 | 5 | 90.0% |
| Innovation, Entrepreneurship, and Career Intentions Assessment | 2 | 4 | 5 | 85.0% |
| Experiential and Active Learning Assessment | 1 | 5 | 5 | 85.0% |
| Sustainability, Ethics, and Leadership Competencies Assessment | 3 | 5 | 5 | 100.0% |
| Assessment Instrument Development and Validation | 4 | 54 | 5 | 100.0% |
| Educational Contexts and Assessment Environments | 1 | 23 | 5 | 88.8% |
| Reflective Practices and Metacognition in Engineering Education | 1 | 1 | 5 | 92.5% |
| Diversity and Inclusion in Engineering Assessment | 1 | 4 | 5 | 96.3% |
| Mathematical and Technical Competency Assessment | 1 | 2 | 5 | 95.0% |
| Large-Scale and Cross-Cultural Competency Benchmarking | 1 | 3 | 5 | 95.0% |
| Pedagogical Interventions and Learning Outcomes Assessment | 1 | 3 | 5 | 90.0% |
| Writing Attitudes and Academic Performance in Engineering | 1 | 1 | 5 | 100.0% |
| Self-Efficacy in Biomedical Engineering Contexts | 1 | 1 | 5 | 90.0% |
| Educational Assessment Policy and Institutional Impact | 1 | 2 | 5 | 95.0% |

---

## Phase 2: Analytical Axes

### Methodological Rigor in Competency Assessment
- **Coverage:** ~57%
- **Justification:** The majority of studies (54) focus on developing and validating assessment instruments, indicating a strong emphasis on methodological rigor. This axis explores how different themes rely on validated tools to ensure reliability and validity.
- **Research potential:** Could inform best practices for designing and validating assessment tools across diverse competency domains.

### Integration of Non-Technical Skills in Engineering Education
- **Coverage:** ~30%
- **Justification:** Multiple themes (e.g., 'Sustainability, Ethics, and Leadership Competencies Assessment', 'Advanced Cognitive and Systems Thinking Skills Assessment') highlight the growing importance of non-technical skills in engineering curricula.
- **Research potential:** Could guide curriculum development to better align with industry demands for holistic engineering competencies.

### Contextual Variability in Assessment
- **Coverage:** ~25%
- **Justification:** Themes like 'Educational Contexts and Assessment Environments' and 'Experiential and Active Learning Assessment' emphasize the need to tailor assessments to specific learning environments.
- **Research potential:** Could inform the design of context-specific assessment strategies that enhance learning outcomes.

### Equity and Inclusion in Assessment Outcomes
- **Coverage:** ~4%
- **Justification:** The 'Diversity and Inclusion in Engineering Assessment' theme, though smaller in study count, addresses critical gaps in ensuring fair and equitable assessment practices.
- **Research potential:** Could drive policy changes and institutional practices to promote diversity and inclusion in engineering education.

---

## Phase 3: Proposed Frameworks

### Framework 1: Psychometric and Methodological Framework
**Justification:** This framework centers on the dominant theme of assessment instrument development and validation, which underpins nearly all other competency assessments. It reflects the empirical pattern where 54 studies (~57%) focus on methodological rigor in tool creation and validation.

**General Objective:** To analyze the development, validation, and application of assessment instruments across engineering education competencies.

**Specific Objectives:**
- To evaluate the psychometric properties (reliability, validity) of assessment instruments used in engineering competency evaluations.
- To compare the methodological approaches used for assessing technical vs. non-technical competencies in engineering education.
- To assess the contextual variability in instrument validation across different educational environments (e.g., classrooms, internships).

**Coverage:** ~70%

### Framework 2: Competency Integration and Holistic Development Framework
**Justification:** This framework reflects the empirical observation that non-technical competencies (e.g., systems thinking, ethics, leadership) are increasingly integrated into broader competency assessments, as seen in multiple themes (e.g., 30% coverage of non-technical skills).

**General Objective:** To examine the integration of diverse competencies (technical and non-technical) in engineering education and their assessment.

**Specific Objectives:**
- To map the prevalence and assessment methods of non-technical competencies (e.g., sustainability, ethics, leadership) in engineering curricula.
- To analyze the relationship between higher-order cognitive skills (e.g., systems thinking) and professional competencies in engineering practice.
- To evaluate how experiential and active learning strategies contribute to the development of integrated competencies.
- To assess the role of innovation and entrepreneurship in shaping competency frameworks for engineering students.

**Coverage:** ~45%

### Framework 3: Contextual and Equity-Centered Assessment Framework
**Justification:** This framework prioritizes the contextual variability and equity dimensions of assessment, as reflected in themes like 'Educational Contexts and Assessment Environments' (~25% coverage) and 'Diversity and Inclusion in Engineering Assessment' (~4% coverage). It addresses gaps in how assessment practices adapt to diverse settings and populations.

**General Objective:** To analyze how assessment practices vary across educational contexts and address equity and inclusion in engineering education.

**Specific Objectives:**
- To evaluate the design and implementation of assessment strategies tailored to specific educational environments (e.g., classrooms, internships, online learning).
- To assess the inclusivity and fairness of assessment practices across diverse student populations.
- To compare assessment outcomes in different contexts (e.g., technical vs. non-technical competencies) to identify disparities.

**Coverage:** ~30%

---

## Recommendation

The 'Psychometric and Methodological Framework' is recommended because it aligns with the most robust empirical pattern in the data (54 studies on assessment instrument development and validation) and provides a strong foundation for comparative and relational analyses across themes. This framework also directly informs best practices for designing and validating assessment tools, which is critical for advancing engineering education research and practice.

---

## Traceability

This analysis is fully traceable. See:
- Results: `inductive_results_20260724_231535.json`
- Trace log: `logs/trace_20260724_231535.json`
- Cache: `.cache/20260724_231535_*`
- CSV exports: `csv/`