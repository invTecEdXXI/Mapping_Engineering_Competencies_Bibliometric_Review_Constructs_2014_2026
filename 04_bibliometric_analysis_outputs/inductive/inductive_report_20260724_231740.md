# Inductive Thematic Analysis Report

**Session ID:** 20260724_231740
**Date:** 2026-07-24 23:19
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
| Quote Grounding | **72.2%** |
| Article Grounding | **100.0%** |
| Taxonomy Grounding | **100.0%** |
| Theme Reference Grounding | **100.0%** |
| Combined Grounding | **80.5%** |
| Hallucination Flags | 22 |
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

### Engineering Self-Efficacy and Identity
- **Studies:** ~14 (soporte real: 14 articulos)
- **Robustness:** High
- **Definition:** The development, assessment, and validation of instruments to measure students' self-efficacy, identity, and sense of belonging in engineering contexts. This includes both general engineering self-efficacy and domain-specific self-efficacy (e.g., programming, design) as well as broader identity constructs like recognition and interest in engineering.
- **Subthemes:** General and domain-specific self-efficacy in engineering, Engineering identity, belonging, and recognition

### Ethical, Social Responsibility, and Professional Values
- **Studies:** ~5 (soporte real: 5 articulos)
- **Robustness:** High
- **Definition:** The assessment of professional ethics, social responsibility, and dispositional values in engineering students. This includes evaluating understanding of ethical principles, sustainability, and global/societal impacts, as well as professional values aligned with engineering practice.
- **Subthemes:** Professional and ethical values, Sustainability, ethics, and social responsibility competencies

### Motivational and Psychosocial Constructs in Engineering Education
- **Studies:** ~6 (soporte real: 6 articulos)
- **Robustness:** High
- **Definition:** The measurement and validation of instruments assessing students' motivational attitudes, learning strategies, and psychosocial constructs (e.g., self-efficacy, attitudes) and their influence on educational outcomes. This includes both general motivational frameworks and specific constructs tied to engineering education.
- **Subthemes:** Motivational and learning strategies, Psychosocial constructs and their influence on educational outcomes

### Workplace Readiness and Internship Competency Assessment
- **Studies:** ~7 (soporte real: 7 articulos)
- **Robustness:** High
- **Definition:** The development and validation of instruments to assess students' competencies and experiences related to workplace readiness, internships, and alignment with industry expectations. This includes perceptions of internship experiences, employability skills, and readiness for professional practice.
- **Subthemes:** Workplace and internship competency evaluation, Industry and workplace readiness assessment

### Communication and Transferable Competencies
- **Studies:** ~7 (soporte real: 7 articulos)
- **Robustness:** High
- **Definition:** The assessment of communication skills and other non-technical, transferable competencies essential for engineering graduates' employability. This includes workplace oral communication, teamwork, problem-solving, and critical thinking as broadly applicable skills.
- **Subthemes:** Communication skills in engineering contexts, Transferable and vocational competencies

### Assessment Instrument Development and Validation
- **Studies:** ~24 (soporte real: 24 articulos)
- **Robustness:** High
- **Definition:** The process of creating, refining, and validating tools (e.g., scales, rubrics, questionnaires) to measure specific competencies, attitudes, or skills in engineering education. This includes designing instruments, conducting pilot tests, and iteratively improving their structure and content based on empirical evidence.
- **Subthemes:** Psychometric validation, Factor analysis, Reliability testing

### Engineering Competencies and Skills
- **Studies:** ~13 (soporte real: 13 articulos)
- **Robustness:** High
- **Definition:** The identification, assessment, and development of technical and non-technical (transversal) competencies required for engineering students. This encompasses professional skills, research competencies, and other transferable abilities essential for engineering practice.
- **Subthemes:** Professional skills, Transversal competencies, Research competences

### Psychometric Properties and Statistical Analysis
- **Studies:** ~15 (soporte real: 15 articulos)
- **Robustness:** High
- **Definition:** The use of statistical methods to evaluate the validity, reliability, and structural properties of assessment instruments in engineering education. This includes techniques such as Cronbach's alpha, factor analysis, and structural equation modeling to ensure robust measurement.
- **Subthemes:** Reliability testing, Factor analysis, Structural equation modeling

### Entrepreneurial and Design Mindset Assessment
- **Studies:** ~5 (soporte real: 5 articulos)
- **Robustness:** High
- **Definition:** The development and validation of instruments to measure entrepreneurial mindset constructs (e.g., 'Connections' and 'Creating Value') and design mindset in engineering students. This theme captures the intersection of innovation, creativity, and problem-solving in engineering education.
- **Subthemes:** Entrepreneurial mindset, Design mindset, Creativity assessment

### Systems Thinking and Problem-Solving Assessment
- **Studies:** ~7 (soporte real: 7 articulos)
- **Robustness:** High
- **Definition:** The assessment of systems thinking skills and problem-solving competencies in engineering students using surveys and diagnostic activities. This theme emphasizes the ability to analyze complex systems and develop effective solutions.
- **Subthemes:** Systems thinking, Problem-based learning, Diagnostic activities

### Mathematical and Technical Competence Assessment
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** The development and validation of instruments to assess mathematical and technical competencies in engineering students, including the use of Rasch analysis and think-aloud protocols. This theme addresses foundational and advanced technical skills critical to engineering practice.
- **Subthemes:** Mathematical competence, Technical skills, Rasch analysis

### Demographic Influences on Engineering Competencies
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** Medium
- **Definition:** The examination of how gender, class level, transfer status, or other demographic factors influence self-efficacy, problem-solving abilities, or other measured competencies in engineering education. This theme explores disparities and variations in outcomes across different student groups.
- **Subthemes:** Gender disparities, First-generation students, Demographic impacts, Class level differences

### Leadership Competencies and Self-Efficacy in Engineering
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The development and validation of instruments to measure engineering students' leadership self-efficacy, including the identification of key leadership domains relevant to engineering contexts. This theme also examines the relationship between leadership confidence and broader professional competencies.
- **Subthemes:** Leadership development, Self-efficacy measurement, Factor structure and reliability

### Writing Attitudes and Affective Dimensions in Engineering Education
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The study of engineering students' attitudes, emotions, and apprehensions related to academic and professional writing, including the development of tools to assess and address writing challenges. This theme explores the impact of writing attitudes on career trajectories and educational outcomes.
- **Subthemes:** Writing apprehension, Survey validation, Career trajectory implications

### Task-Specific Self-Efficacy in Biomedical Engineering
- **Studies:** ~1 (soporte real: 1 articulos)
- **Robustness:** Medium
- **Definition:** The measurement of engineering students' confidence in performing specific tasks within biomedical engineering contexts, such as problem identification, engineering solutions, and grant proposal writing. This theme emphasizes the clinical and technical relevance of self-efficacy assessments.
- **Subthemes:** Task-specific confidence, Clinical relevance, Survey design for biomedical contexts

### Structural Signatures (Mejora 5)

| Theme | Source Batches | Articles | Quotes | Combined Grounding |
|-------|--------------|----------|--------|-------------------|
| Engineering Self-Efficacy and Identity | 3 | 14 | 5 | 92.5% |
| Ethical, Social Responsibility, and Professional Values | 2 | 5 | 5 | 92.5% |
| Motivational and Psychosocial Constructs in Engineering Education | 2 | 6 | 5 | 92.5% |
| Workplace Readiness and Internship Competency Assessment | 2 | 7 | 5 | 85.0% |
| Communication and Transferable Competencies | 2 | 7 | 5 | 85.0% |
| Assessment Instrument Development and Validation | 3 | 24 | 5 | 100.0% |
| Engineering Competencies and Skills | 2 | 13 | 5 | 100.0% |
| Psychometric Properties and Statistical Analysis | 2 | 15 | 5 | 100.0% |
| Entrepreneurial and Design Mindset Assessment | 2 | 5 | 5 | 100.0% |
| Systems Thinking and Problem-Solving Assessment | 2 | 7 | 5 | 100.0% |
| Mathematical and Technical Competence Assessment | 1 | 2 | 5 | 100.0% |
| Demographic Influences on Engineering Competencies | 1 | 4 | 5 | 96.3% |
| Leadership Competencies and Self-Efficacy in Engineering | 1 | 1 | 5 | 100.0% |
| Writing Attitudes and Affective Dimensions in Engineering Education | 1 | 1 | 5 | 100.0% |
| Task-Specific Self-Efficacy in Biomedical Engineering | 1 | 1 | 5 | 90.0% |

---

## Phase 2: Analytical Axes

### Psychometric Rigor in Engineering Education Assessment
- **Coverage:** ~40%
- **Justification:** A significant portion of studies (n=24) focus on instrument development and validation, often paired with psychometric analysis (n=15). This axis highlights the importance of rigorous measurement tools in engineering education research.
- **Research potential:** Could inform best practices for developing and validating assessment instruments, ensuring they are reliable and valid for diverse engineering contexts.

### Non-Technical Competencies and Employability
- **Coverage:** ~27%
- **Justification:** Themes like Communication and Transferable Competencies (n=7), Workplace Readiness (n=7), and Engineering Competencies and Skills (n=13) emphasize the growing importance of soft skills in engineering education.
- **Research potential:** Could guide curriculum design to better integrate transferable skills, addressing industry demands for well-rounded engineers.

### Self-Efficacy and Identity Development
- **Coverage:** ~20%
- **Justification:** Engineering Self-Efficacy and Identity (n=14) and its association with motivational constructs (n=6) suggest a strong focus on students' confidence and belonging in engineering.
- **Research potential:** Could explore interventions to enhance self-efficacy and identity, particularly for underrepresented groups, to improve retention and success.

### Ethics and Social Responsibility in Engineering Practice
- **Coverage:** ~10%
- **Justification:** Ethical, Social Responsibility, and Professional Values (n=5) is a critical but understudied theme, with potential links to demographic influences (n=4).
- **Research potential:** Could investigate how ethical training impacts career trajectories and professional identity, particularly across diverse student populations.

---

## Phase 3: Proposed Frameworks

### Framework 1: Psychometric and Competency Integration Framework
**Justification:** This framework aligns with the high coverage of instrument development (n=24) and psychometric analysis (n=15), while also integrating competency-based themes (e.g., Engineering Competencies and Skills, Communication and Transferable Competencies). It reflects the empirical pattern of rigorous measurement tools being central to assessing both technical and non-technical competencies.

**General Objective:** To integrate psychometric rigor with competency-based assessment in engineering education, examining how measurement tools and competency frameworks collectively inform educational outcomes and employability.

**Specific Objectives:**
- To analyze the development, validation, and psychometric properties of assessment instruments in engineering education.
- To evaluate the role of technical and non-technical competencies (e.g., communication, problem-solving) in shaping engineering education outcomes.
- To assess the relationship between instrument validity and the reliability of competency assessments in engineering contexts.
- To identify gaps in the alignment between psychometric tools and competency frameworks in engineering education research.

**Coverage:** ~63%

### Framework 2: Student Development and Employability Framework
**Justification:** This framework is grounded in the strong focus on self-efficacy (n=14), motivational constructs (n=6), and workplace readiness (n=7). It reflects the empirical pattern of student development being closely tied to employability and industry expectations, particularly in non-technical domains.

**General Objective:** To examine how student development in engineering (e.g., self-efficacy, identity, motivation) and employability competencies (e.g., communication, workplace readiness) interact to shape educational and career outcomes.

**Specific Objectives:**
- To assess the development of engineering self-efficacy, identity, and motivational constructs among students.
- To evaluate the role of transferable competencies (e.g., communication, teamwork) in preparing students for workplace readiness.
- To explore the relationship between student development (e.g., self-efficacy) and employability outcomes (e.g., internship success).
- To identify demographic or contextual factors influencing student development and employability.

**Coverage:** ~40-50%

### Framework 3: Ethical, Social, and Professional Responsibility Framework
**Justification:** This framework is designed to address the underrepresented but critical theme of ethics and social responsibility (n=5), while also integrating related constructs like professional values and demographic influences (n=4). It reflects the empirical pattern of these themes being less studied but highly relevant to engineering practice.

**General Objective:** To examine the role of ethical, social responsibility, and professional values in engineering education, and their impact on student development, employability, and career trajectories.

**Specific Objectives:**
- To assess the development and assessment of ethical, social responsibility, and professional values in engineering students.
- To evaluate the relationship between ethical training and students' professional identity, self-efficacy, and employability.
- To explore demographic influences on ethical decision-making, social responsibility, and professional values in engineering.
- To identify gaps in the integration of ethical and social responsibility training within engineering curricula.

**Coverage:** ~10-20%

---

## Recommendation

The 'Psychometric and Competency Integration Framework' is recommended as the primary analytical framework. It aligns with the most robust themes in the dataset (e.g., instrument development, psychometric analysis, and competency assessment), covers a significant portion of the studies (~63%), and allows for both descriptive and comparative analyses. This framework also addresses both technical and non-technical competencies, reflecting the dual priorities of engineering education research and industry demands. While the other frameworks offer valuable insights, they either cover less empirical ground (e.g., Ethical, Social, and Professional Responsibility Framework) or focus narrowly on student development (e.g., Student Development and Employability Framework). The Psychometric and Competency Integration Framework provides a more comprehensive and balanced approach to organizing the systematic review's findings.

---

## Traceability

This analysis is fully traceable. See:
- Results: `inductive_results_20260724_231740.json`
- Trace log: `logs/trace_20260724_231740.json`
- Cache: `.cache/20260724_231740_*`
- CSV exports: `csv/`