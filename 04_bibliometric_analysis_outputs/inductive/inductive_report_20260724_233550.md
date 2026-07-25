# Inductive Thematic Analysis Report

**Session ID:** 20260724_233550
**Date:** 2026-07-24 23:48
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
| Quote Grounding | **81.0%** |
| Article Grounding | **100.0%** |
| Taxonomy Grounding | **100.0%** |
| Theme Reference Grounding | **100.0%** |
| Combined Grounding | **86.7%** |
| Hallucination Flags | 13 |
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

### Instrument Development and Psychometric Validation in Engineering Education
- **Studies:** ~64 (soporte real: 64 articulos)
- **Robustness:** High
- **Definition:** This theme encompasses research focused on the design, adaptation, and rigorous psychometric testing of measurement instruments such as scales, questionnaires, and rubrics. Studies often involve scale adaptation, factor analysis, reliability analysis, construct validity, and content validation to ensure robust measurement.
- **Subthemes:** scale adaptation, factor analysis, reliability, construct validity, content validation

### Assessment of Generic, Transversal, and Professional Competencies
- **Studies:** ~13 (soporte real: 13 articulos)
- **Robustness:** High
- **Definition:** Research that develops or validates instruments to measure broad professional skills often called generic or transversal competencies, such as teamwork, communication, lifelong learning, and workplace adaptability. These competencies are crucial for 21st-century engineers.
- **Subthemes:** professional skills, 21st century skills, transversal competencies, workplace adaptability, innovation competence

### Self-Efficacy and Engineering Identity Measurement
- **Studies:** ~16 (soporte real: 16 articulos)
- **Robustness:** High
- **Definition:** Studies aimed at creating and validating scales that capture engineering students' beliefs about their capabilities (self-efficacy) in specific skill areas (entrepreneurship, design) and their sense of engineering identity, which relates to career persistence.
- **Subthemes:** engineering identity, entrepreneurial self-efficacy, design self-efficacy, career persistence

### Attitudes Toward Engineering and Practical Learning Experiences
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** Medium
- **Definition:** Research that quantitatively assesses engineering students' attitudes toward practical work, the sociotechnical nature of the discipline, and the learning of professional skills. It often examines factor structures underlying these attitudes.
- **Subthemes:** practical work, sociotechnical engineering, professional skills attitudes, factor structure

### Rubric-Based Competency Assessment
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** Medium
- **Definition:** A body of work that centers on the design, validation, and use of scoring rubrics to evaluate student competencies in engineering contexts, including laboratories, oral presentations, and design projects. Content validity is established through expert judgment, and inter-rater reliability is assessed.
- **Subthemes:** scoring rubric, content validity, expert judgment, inter-rater reliability, competency-based assessment

### Research Competences and Investigative Skills
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** Studies that identify and measure the research skills required by engineering students, often for completing final projects. Instruments assess multiple dimensions such as intellectual and communicative competences.
- **Subthemes:** research training, End of Studies Projects, intellectual competences, communicative competences

### Critical, Reflective, and Representational Thinking Assessment
- **Studies:** ~7 (soporte real: 7 articulos)
- **Robustness:** High
- **Definition:** Instruments developed to measure higher-order cognitive skills in engineering, including critical thinking in automation control, reflective thinking during design problem solving, and representational competence in using multiple representations.
- **Subthemes:** critical thinking, reflection, design problem solving, representational competence, multiple representations

### Affective and Ethical Competence Assessment
- **Studies:** ~2 (soporte real: 2 articulos)
- **Robustness:** Medium
- **Definition:** Research targeting the assessment of values, compassion, and socio-emotional competencies in engineering students. These studies adapt instruments from psychology (e.g., Compassion Scale) to the engineering context, exploring the affective domain and dispositional knowledge.
- **Subthemes:** compassion, professional values, affective domain, socio-emotional competency, dispositional knowledge

### Motivation and Engagement in Engineering Education
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** Medium
- **Definition:** Instruments assessing students’ motivational attitudes (intrinsic/extrinsic), behaviors, self-regulation, and value perceptions, which influence their effectiveness, persistence, and engagement in engineering learning contexts. These measures draw on frameworks such as expectancy-value theory and self-determination theory.
- **Subthemes:** intrinsic motivation, extrinsic motivation, self-regulation, expectancy-value theory, persistence intentions

### Mindset and Dispositional Factors in Engineering
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** Non-cognitive constructs such as design mindset, entrepreneurial mindset, grit, and ambiguity tolerance that encompass iterative thinking, creativity, and perseverance, and are measured to understand students’ dispositions towards engineering challenges. These instruments often target both general and domain-specific mindsets.
- **Subthemes:** design mindset, entrepreneurial mindset, grit, ambiguity tolerance, iteration

### Learning Environment and Pedagogical Practices Assessment
- **Studies:** ~6 (soporte real: 6 articulos)
- **Robustness:** Medium
- **Definition:** Development and validation of instruments evaluating the impact of specific educational settings—such as community-partnered projects, internships/apprenticeships, active learning environments, and peer assessment—on student outcomes in engineering education. These tools examine both the design and the perceived effectiveness of the pedagogy.
- **Subthemes:** community-partnered projects, internship, apprenticeship, active learning, peer assessment

### Factor Analysis as Primary Validation Method
- **Studies:** ~4 (soporte real: 4 articulos)
- **Robustness:** Medium
- **Definition:** Factor analysis, both exploratory and confirmatory, is consistently employed as the primary method for uncovering underlying factor structures, reducing items, and establishing construct validity of newly developed instruments. Studies focus on psychometric properties such as Cronbach's alpha and use techniques like principal axis factoring to ensure reliability and validity.
- **Subthemes:** Exploratory Factor Analysis, Confirmatory Factor Analysis, Reliability Assessment via Cronbach's Alpha

### Linking Student Attributes to Career Intentions and Professional Outcomes
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** This theme captures research that explicitly links measured non-cognitive and motivational attributes—such as self-efficacy, writing attitudes, and entrepreneurial motivation—to career-related outcomes including entrepreneurial intention, persistence, and professional skill application. Studies typically establish predictive or mediating relationships between these attributes and indicators of career success.
- **Subthemes:** Entrepreneurial Intention, Academic and Professional Persistence, Skill-Specific Outcomes (e.g., grant writing)

### Affective and Motivational Factors in Professional Skill Development
- **Studies:** ~3 (soporte real: 3 articulos)
- **Robustness:** Medium
- **Definition:** Studies in this theme examine how emotions, personal interests, and motivation influence the development of professional skills in engineering students. It includes investigations of affective barriers such as writing apprehension and writer's block, as well as intrinsic motivators like personal interests and team motivation.
- **Subthemes:** Writing Apprehension and Writer's Block, Personal Interests and Intrinsic Motivation, Motivational Drivers in Team Settings

### Structural Signatures (Mejora 5)

| Theme | Source Batches | Articles | Quotes | Combined Grounding |
|-------|--------------|----------|--------|-------------------|
| Instrument Development and Psychometric Validation in Engineering Education | 3 | 64 | 5 | 100.0% |
| Assessment of Generic, Transversal, and Professional Competencies | 2 | 13 | 5 | 100.0% |
| Self-Efficacy and Engineering Identity Measurement | 3 | 16 | 5 | 100.0% |
| Attitudes Toward Engineering and Practical Learning Experiences | 1 | 4 | 5 | 100.0% |
| Rubric-Based Competency Assessment | 1 | 4 | 5 | 100.0% |
| Research Competences and Investigative Skills | 1 | 2 | 5 | 100.0% |
| Critical, Reflective, and Representational Thinking Assessment | 2 | 7 | 5 | 100.0% |
| Affective and Ethical Competence Assessment | 1 | 2 | 5 | 100.0% |
| Motivation and Engagement in Engineering Education | 1 | 4 | 5 | 100.0% |
| Mindset and Dispositional Factors in Engineering | 1 | 3 | 5 | 100.0% |
| Learning Environment and Pedagogical Practices Assessment | 1 | 6 | 5 | 100.0% |
| Factor Analysis as Primary Validation Method | 1 | 4 | 5 | 100.0% |
| Linking Student Attributes to Career Intentions and Professional Outcomes | 1 | 3 | 5 | 90.0% |
| Affective and Motivational Factors in Professional Skill Development | 1 | 3 | 5 | 90.0% |

---

## Phase 2: Analytical Axes

### Methodological Rigor vs. Construct Exploration
- **Coverage:** 80%
- **Justification:** Many studies emphasize psychometric validation (factor analysis, reliability) while others focus on defining and measuring new constructs. This axis distinguishes between advancing measurement science and extending the substantive scope of engineering education research.
- **Research potential:** Helps identify which constructs lack rigorous measurement and which methods could be transferred to under-explored domains (e.g., ethical/affective competencies).

### Cognitive/Behavioral vs. Affective/Dispositional Assessment
- **Coverage:** 65%
- **Justification:** Themes split between assessing observable skills (critical thinking, professional competencies) and internal states (motivation, mindset, identity). This axis allows analysis of how the field balances competency-based education with whole-person development.
- **Research potential:** Underscores the need for integrated frameworks that capture the interplay between skill and disposition, informing holistic curriculum design.

### Descriptive Measurement vs. Predictive/Causal Modeling
- **Coverage:** 50%
- **Justification:** Most studies stop at instrument validation or descriptive measurement, while a smaller set explicitly models relationships to career outcomes. This axis reveals the extent to which research moves from diagnosis to forecasting or intervention.
- **Research potential:** Encourages longitudinal and predictive studies that validate instruments against real-world professional performance, not just academic proxies.

---

## Phase 3: Proposed Frameworks

### Framework 1: Measurement Process and Instrument Validation Lifecycle
**Justification:** The systematic review reveals a dominant focus on instrument development and psychometric validation, with factor analysis and rubric-based methods as complementary approaches. Organizing findings around the validation lifecycle highlights methodological rigor and allows comparative analysis of validation practices.

**General Objective:** To synthesize and compare the processes of instrument design, content validation, construct validation, and reliability testing across engineering education assessment research.

**Specific Objectives:**
- Examine instrument design and content validation processes, including expert judgment and rubric development.
- Compare factor structures and construct validity methods (EFA/CFA) across instruments.
- Evaluate reliability and inter-rater reliability evidence in rubric-based and psychometric assessments.

**Coverage:** 75%

### Framework 2: Substantive Assessment Domains for Engineering Learner Development
**Justification:** The emergent themes cluster around distinct types of constructs: cognitive skills, professional competencies, self-beliefs, and affective/motivational factors. This framework maps what is actually being measured, revealing coverage gaps and enabling targeted curriculum improvement.

**General Objective:** To map the landscape of measured constructs in engineering education, categorize them into coherent domains, and evaluate their assessment instruments.

**Specific Objectives:**
- Characterize instruments measuring cognitive, critical, and investigative thinking skills.
- Assess the validity and structure of instruments for professional, transversal, and generic competencies, including attitudes toward practical work.
- Examine how self-efficacy and engineering identity scales predict career intentions and professional outcomes.
- Investigate instruments targeting affective, ethical, motivational, and mindset constructs in engineering education.

**Coverage:** 85%

### Framework 3: From Measurement to Impact: Predictive Relationships and Practical Outcomes
**Justification:** While most research focuses on instrument validation or descriptive measurement, a critical subset models the predictive links from student attributes and learning environments to career intentions and skill development. This framework emphasizes the practical utility of measurement for educational intervention.

**General Objective:** To trace the predictive pathways through which measured student attributes, motivations, and learning environments influence professional skill development and career outcomes in engineering.

**Specific Objectives:**
- Model the predictive relationship between self-efficacy, engineering identity, and career intentions/persistence.
- Analyze the role of motivation and affective factors in professional skill acquisition and development.
- Investigate how learning environments and pedagogical practices predict student attitudes and competencies.
- Assess the psychometric foundations (factor structure, reliability) required for valid predictive modeling in engineering education.

**Coverage:** 30%

---

## Recommendation

I recommend the 'Substantive Assessment Domains for Engineering Learner Development' framework because it achieves the highest coverage (85%), organizes findings around what is actually being measured, and aligns with the cognitive/affective analytical axis. It offers clear value for curriculum designers, assessment developers, and researchers seeking to identify gaps—particularly the underrepresentation of affective, ethical, and motivational assessments—while remaining grounded in the robust empirical patterns of the review.

---

## Traceability

This analysis is fully traceable. See:
- Results: `inductive_results_20260724_233550.json`
- Trace log: `logs/trace_20260724_233550.json`
- Cache: `.cache/20260724_233550_*`
- CSV exports: `csv/`