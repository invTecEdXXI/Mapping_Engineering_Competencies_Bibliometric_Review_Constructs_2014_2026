# Inductive Thematic Analysis Report

**Session ID:** 20260724_234822
**Date:** 2026-07-24 23:52
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
| Quote Grounding | **85.2%** |
| Article Grounding | **100.0%** |
| Taxonomy Grounding | **100.0%** |
| Theme Reference Grounding | **100.0%** |
| Combined Grounding | **89.6%** |
| Hallucination Flags | 15 |
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

### Validation and Use of Competency Assessment Instruments in Engineering Education
- **Studies:** ~71 (soporte real: 71 articulos)
- **Robustness:** High
- **Definition:** The development, validation, and application of assessment tools such as scales, rubrics, or questionnaires to measure specific competencies, skills, or attitudes in engineering students. This includes statistical validation, expert judgment, and the use of these instruments in laboratory, project-based, or classroom settings.
- **Subthemes:** Psychometric validation of competency assessment instruments, Rubric-based competency assessment and validation

### Self-Efficacy and Learning Experiences in Engineering Education
- **Studies:** ~30 (soporte real: 30 articulos)
- **Robustness:** High
- **Definition:** The measurement of students' confidence or belief in their ability to perform specific tasks (self-efficacy) and the assessment of learning experiences (e.g., performance accomplishments, vicarious learning) that contribute to its development. This includes the exploration of how these factors influence career-related outcomes and affective traits in engineering contexts.
- **Subthemes:** Self-efficacy and attitudes in engineering contexts, Learning experiences and sources of self-efficacy

### Professional, Ethical, and Generic Competencies in Engineering Education
- **Studies:** ~22 (soporte real: 22 articulos)
- **Robustness:** High
- **Definition:** The assessment and development of non-technical or soft skills (e.g., communication, teamwork, leadership, problem-solving) alongside professional and ethical competencies in engineering students. This includes the evaluation of students' understanding and application of ethical standards, social responsibility, and professional conduct in engineering practice.
- **Subthemes:** Generic and professional competencies in engineering education, Assessment of professional and ethical competencies in engineering

### Socio-Emotional and Psychological Competencies in Engineering Education
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** The exploration and validation of socio-emotional and psychological constructs such as resilience, optimism, adaptability, compassion, and empathy in engineering education. This includes their impact on academic performance, retention, ethical reasoning, and overall success in engineering students.
- **Subthemes:** Resilience and psychological factors in engineering education, Compassion and socio-emotional competencies in engineering

### Motivational and Career-Related Constructs in Engineering Education
- **Studies:** ~9 (soporte real: 9 articulos)
- **Robustness:** High
- **Definition:** The study of students' intrinsic and extrinsic motivations, attitudes, learning strategies, and career-related trajectories in engineering contexts. This includes the development of instruments to measure these constructs and the exploration of factors influencing career choices, intentions, and leadership development.
- **Subthemes:** Motivational attitudes and behaviors in engineering education, Career-related constructs and trajectories in engineering students

### Representational Competence in Engineering
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The ability of students to interpret, switch between, and use multiple representations (e.g., diagrams, symbols, narrative language) of engineering concepts, particularly in problem-solving contexts. This competence is critical for conceptual understanding and effective communication in engineering.
- **Subthemes:** Vector representations, Problem-solving, Conceptual understanding

### Research Competencies in Engineering Education
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The assessment and development of research-related skills and competencies in engineering students, including investigative skills, scientific writing, and research training. These competencies encompass intellectual, technical, and communicative aspects of research projects.
- **Subthemes:** Investigative skills, Scientific writing, Research training

### Critical Thinking and Decision-Making in Engineering
- **Studies:** ~6 (soporte real: 6 articulos)
- **Robustness:** High
- **Definition:** The development and validation of instruments to assess critical thinking and decision-making competencies in engineering students. This often occurs in the context of specific technical or professional problem-solving scenarios.
- **Subthemes:** Critical thinking assessment, Decision-making competency, Problem-solving

### Systems Thinking and Problem-Solving in Engineering
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The assessment of students' ability to approach complex engineering problems holistically, considering interdependencies and broader systems. This theme includes the development of tools to evaluate design mindset, iterative problem-solving, and competency in handling complex systems.
- **Subthemes:** Design mindset, Iterative problem-solving, Complex systems

### Impact of Experiential Learning on Engineering Student Outcomes
- **Studies:** ~8 (soporte real: 8 articulos)
- **Robustness:** High
- **Definition:** The exploration of how hands-on, real-world learning experiences such as internships, community-partnered projects, and apprenticeships influence the development of students' skills, self-efficacy, and professional readiness. This includes the assessment of workplace learning and its role in shaping career trajectories.
- **Subthemes:** Internship evaluation, Community engagement, Workplace learning

### Gender Differences in Engineering Competencies and Self-Efficacy
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** Medium
- **Definition:** The exploration of differences between male and female engineering students in terms of self-efficacy, competencies, affective traits, and academic performance. This includes studies investigating gendered experiences, self-efficacy gaps, and their implications for engineering education and career outcomes.
- **Subthemes:** Gendered experiences in engineering education, Self-efficacy gaps between male and female students, Impact of gender on academic performance and retention

### Sustainability and Ethics Competencies in Engineering Education
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The integration of sustainability, ethics, and social responsibility into engineering curricula, and the assessment of these competencies among engineering students. This theme includes the development of tools and frameworks to measure students' understanding and application of ethical principles and sustainability practices.
- **Subthemes:** Curricular integration of sustainability and ethics, Assessment of ethical reasoning in engineering, Sustainability learning outcomes

### Innovation and Entrepreneurship Competencies in Engineering
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The measurement and development of innovation self-efficacy and entrepreneurial competencies among engineering students. This includes the creation and validation of scales to assess these competencies and their role in career development and engineering practice.
- **Subthemes:** Innovation self-efficacy, Entrepreneurial competencies, Career development and engineering innovation

### Measurement Invariance and Fairness in Engineering Education Assessments
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The examination of whether assessment instruments function similarly across different subpopulations of engineering students, such as first-generation college students or underrepresented groups. This theme includes studies on fairness, equity, and the development of inclusive assessment practices in engineering education.
- **Subthemes:** Fairness in competency assessments, Engineering identity and assessment, Inclusive assessment practices

### Metacognitive and Learning Orientation Tools in Engineering Education
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The creation and validation of tools designed to measure metacognitive skills, learning orientations, and self-regulated learning among engineering students. This theme includes the development of instruments to assess how students plan, monitor, and evaluate their own learning processes in engineering contexts.
- **Subthemes:** Metacognitive processes in engineering learning, Learning orientations and self-regulated learning, Development of metacognitive assessment tools

### Statistical Mediation and Correlation in Engineering Education Research
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The application of statistical methods such as mediation analysis and correlation to explore and explain relationships between variables in engineering education. This includes examining how constructs like self-efficacy, motivation, or attitudes influence outcomes such as career intentions or academic performance.
- **Subthemes:** Mediation effects in engineering education, Correlation analysis of affective and cognitive constructs, Predictive modeling of career trajectories

### Structural Signatures (Mejora 5)

| Theme | Source Batches | Articles | Quotes | Combined Grounding |
|-------|--------------|----------|--------|-------------------|
| Validation and Use of Competency Assessment Instruments in Engineering Education | 4 | 71 | 5 | 92.5% |
| Self-Efficacy and Learning Experiences in Engineering Education | 4 | 30 | 5 | 100.0% |
| Professional, Ethical, and Generic Competencies in Engineering Education | 3 | 22 | 5 | 85.0% |
| Socio-Emotional and Psychological Competencies in Engineering Education | 1 | 3 | 5 | 85.0% |
| Motivational and Career-Related Constructs in Engineering Education | 2 | 9 | 5 | 85.0% |
| Representational Competence in Engineering | 1 | 2 | 5 | 100.0% |
| Research Competencies in Engineering Education | 1 | 2 | 5 | 100.0% |
| Critical Thinking and Decision-Making in Engineering | 2 | 6 | 5 | 100.0% |
| Systems Thinking and Problem-Solving in Engineering | 1 | 2 | 5 | 100.0% |
| Impact of Experiential Learning on Engineering Student Outcomes | 2 | 8 | 5 | 100.0% |
| Gender Differences in Engineering Competencies and Self-Efficacy | 1 | 4 | 5 | 85.0% |
| Sustainability and Ethics Competencies in Engineering Education | 1 | 2 | 5 | 90.0% |
| Innovation and Entrepreneurship Competencies in Engineering | 1 | 2 | 5 | 95.0% |
| Measurement Invariance and Fairness in Engineering Education Assessments | 1 | 1 | 5 | 90.0% |
| Metacognitive and Learning Orientation Tools in Engineering Education | 1 | 1 | 5 | 90.0% |
| Statistical Mediation and Correlation in Engineering Education Research | 1 | 2 | 5 | 85.0% |

---

## Phase 2: Analytical Axes

---

## Phase 3: Proposed Frameworks

### Framework 1: Competency Assessment and Validation Framework
**Justification:** This framework emphasizes the dominant theme of instrument validation and competency assessment, which is the most robust and frequently occurring topic in the data. It integrates related themes such as self-efficacy and professional competencies, which are often measured using validated instruments, allowing for a cohesive analysis of how competencies are assessed and developed in engineering education.

**General Objective:** To synthesize and evaluate the development, validation, and application of competency assessment instruments in engineering education, and their role in measuring and enhancing student outcomes.

**Specific Objectives:**
- Examine the psychometric properties and validation processes of competency assessment instruments used in engineering education.
- Compare how validated instruments are used to measure self-efficacy and learning experiences in engineering students, and their impact on academic and career outcomes.
- Analyze the assessment of professional, ethical, and generic competencies in engineering education using validated tools, and their relationship to student performance and professional readiness.
- Explore the role of socio-emotional and motivational constructs in engineering education, as measured by validated instruments, and their influence on student retention and success.

**Coverage:** 90-100%

### Framework 2: Student-Centered Competency Development Framework
**Justification:** This framework shifts the focus to the student experience, organizing findings around how competencies, self-efficacy, and socio-emotional factors develop in engineering education. It highlights the interplay between learning experiences, motivational constructs, and competency assessment, providing a holistic view of student outcomes.

**General Objective:** To explore how engineering students develop and demonstrate competencies, self-efficacy, and socio-emotional skills, and the role of learning experiences and assessment instruments in this process.

**Specific Objectives:**
- Investigate the sources and development of self-efficacy in engineering students, and how learning experiences contribute to its growth.
- Assess the development and measurement of professional, ethical, and generic competencies in engineering students, and their alignment with industry expectations.
- Examine the role of socio-emotional and psychological competencies in engineering education, and their impact on academic performance, retention, and ethical reasoning.
- Analyze how motivational and career-related constructs influence engineering students' learning strategies, career choices, and leadership development.

**Coverage:** 60-70%

### Framework 3: Integrated Competency and Assessment Framework
**Justification:** This framework balances the dominant theme of instrument validation with the broader context of competency development, creating a bridge between assessment practices and student outcomes. It allows for an integrated analysis of how validated tools are used to measure and enhance a wide range of competencies, from technical to socio-emotional.

**General Objective:** To analyze the interplay between competency assessment instruments and the development of diverse competencies in engineering education, with a focus on how validated tools inform teaching, learning, and student success.

**Specific Objectives:**
- Evaluate the development, validation, and application of competency assessment instruments in engineering education, and their effectiveness in measuring student outcomes.
- Compare the measurement of self-efficacy and professional competencies using validated instruments, and their relationship to student performance and career readiness.
- Explore the role of motivational and socio-emotional constructs in engineering education, as measured by validated instruments, and their influence on student engagement and retention.
- Assess the impact of experiential learning and ethical training on the development of professional and representational competencies in engineering students.

**Coverage:** 80-90%

---

## Recommendation

Integrated Competency and Assessment Framework ['This framework provides the best balance between the dominant theme of instrument validation and the broader context of competency development in engineering education.', 'It offers high coverage (80-90%) of the studies while allowing for comparative and relational analysis across multiple themes.', 'The framework is grounded in robust empirical patterns and enables a comprehensive synthesis of how assessment tools are used to measure and enhance diverse competencies, from self-efficacy to professional and socio-emotional skills.', 'It also accommodates less studied themes (e.g., representational competence) without overemphasizing them, ensuring a well-rounded analysis.']

---

## Traceability

This analysis is fully traceable. See:
- Results: `inductive_results_20260724_234822.json`
- Trace log: `logs/trace_20260724_234822.json`
- Cache: `.cache/20260724_234822_*`
- CSV exports: `csv/`