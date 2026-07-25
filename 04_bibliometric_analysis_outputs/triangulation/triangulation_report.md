# LLM Triangulation Report

**Generated:** 2026-07-24 23:52
**Model A:** auto/deepseek-v4-pro
**Model B:** mistral/mistral-large-latest

---

## Executive Summary

### Phase 2e: Inductive Topic Discovery

- **Themes discovered (Model A):** 14
- **Themes discovered (Model B):** 16
- **Jaccard similarity (names):** 0.2921
- **Jaccard similarity (definitions):** 0.2475
- **Subtopic overlap:** 0.0198
- **Matched themes (greedy):** 13

**Grounding scores:**

- Model A: 87%
- Model B: 90%

---

---

## Phase 2e: Detailed Results

### Greedy Theme Matching

| Theme (Model A) | Theme (Model B) | Sim (name) | Sim (def) | Sim (combined) |
|-----------------|-----------------|------------|-----------|----------------|
| Motivation and Engagement in Engineering Education | Motivational and Career-Related Constructs in Engineering Education | 0.400 | 0.207 | 0.323 |
| Self-Efficacy and Engineering Identity Measurement | Self-Efficacy and Learning Experiences in Engineering Education | 0.400 | 0.194 | 0.317 |
| Instrument Development and Psychometric Validation in Engineering Education | Validation and Use of Competency Assessment Instruments in Engineering Education | 0.385 | 0.203 | 0.312 |
| Assessment of Generic, Transversal, and Professional Competencies | Professional, Ethical, and Generic Competencies in Engineering Education | 0.364 | 0.119 | 0.266 |
| Critical, Reflective, and Representational Thinking Assessment | Critical Thinking and Decision-Making in Engineering | 0.300 | 0.204 | 0.262 |
| Mindset and Dispositional Factors in Engineering | Innovation and Entrepreneurship Competencies in Engineering | 0.333 | 0.107 | 0.243 |
| Attitudes Toward Engineering and Practical Learning Experiences | Metacognitive and Learning Orientation Tools in Engineering Education | 0.250 | 0.135 | 0.204 |
| Affective and Motivational Factors in Professional Skill Development | Measurement Invariance and Fairness in Engineering Education Assessments | 0.143 | 0.228 | 0.177 |
| Research Competences and Investigative Skills | Research Competencies in Engineering Education | 0.111 | 0.220 | 0.154 |
| Learning Environment and Pedagogical Practices Assessment | Impact of Experiential Learning on Engineering Student Outcomes | 0.077 | 0.259 | 0.150 |
| Affective and Ethical Competence Assessment | Representational Competence in Engineering | 0.125 | 0.164 | 0.141 |
| Linking Student Attributes to Career Intentions and Professional Outcomes | Statistical Mediation and Correlation in Engineering Education Research | 0.062 | 0.250 | 0.138 |
| Rubric-Based Competency Assessment | Systems Thinking and Problem-Solving in Engineering | 0.000 | 0.136 | 0.054 |

### Taxonomy Comparison

**Model A (auto/deepseek-v4-pro):** 14 themes

- **Instrument Development and Psychometric Validation in Engineering Education**: This theme encompasses research focused on the design, adaptation, and rigorous psychometric testing...
- **Assessment of Generic, Transversal, and Professional Competencies**: Research that develops or validates instruments to measure broad professional skills often called ge...
- **Self-Efficacy and Engineering Identity Measurement**: Studies aimed at creating and validating scales that capture engineering students' beliefs about the...
- **Attitudes Toward Engineering and Practical Learning Experiences**: Research that quantitatively assesses engineering students' attitudes toward practical work, the soc...
- **Rubric-Based Competency Assessment**: A body of work that centers on the design, validation, and use of scoring rubrics to evaluate studen...
- **Research Competences and Investigative Skills**: Studies that identify and measure the research skills required by engineering students, often for co...
- **Critical, Reflective, and Representational Thinking Assessment**: Instruments developed to measure higher-order cognitive skills in engineering, including critical th...
- **Affective and Ethical Competence Assessment**: Research targeting the assessment of values, compassion, and socio-emotional competencies in enginee...
- **Motivation and Engagement in Engineering Education**: Instruments assessing students’ motivational attitudes (intrinsic/extrinsic), behaviors, self-regula...
- **Mindset and Dispositional Factors in Engineering**: Non-cognitive constructs such as design mindset, entrepreneurial mindset, grit, and ambiguity tolera...
- **Learning Environment and Pedagogical Practices Assessment**: Development and validation of instruments evaluating the impact of specific educational settings—suc...
- **Factor Analysis as Primary Validation Method**: Factor analysis, both exploratory and confirmatory, is consistently employed as the primary method f...
- **Linking Student Attributes to Career Intentions and Professional Outcomes**: This theme captures research that explicitly links measured non-cognitive and motivational attribute...
- **Affective and Motivational Factors in Professional Skill Development**: Studies in this theme examine how emotions, personal interests, and motivation influence the develop...

**Model B (mistral/mistral-large-latest):** 16 themes

- **Validation and Use of Competency Assessment Instruments in Engineering Education**: The development, validation, and application of assessment tools such as scales, rubrics, or questio...
- **Self-Efficacy and Learning Experiences in Engineering Education**: The measurement of students' confidence or belief in their ability to perform specific tasks (self-e...
- **Professional, Ethical, and Generic Competencies in Engineering Education**: The assessment and development of non-technical or soft skills (e.g., communication, teamwork, leade...
- **Socio-Emotional and Psychological Competencies in Engineering Education**: The exploration and validation of socio-emotional and psychological constructs such as resilience, o...
- **Motivational and Career-Related Constructs in Engineering Education**: The study of students' intrinsic and extrinsic motivations, attitudes, learning strategies, and care...
- **Representational Competence in Engineering**: The ability of students to interpret, switch between, and use multiple representations (e.g., diagra...
- **Research Competencies in Engineering Education**: The assessment and development of research-related skills and competencies in engineering students, ...
- **Critical Thinking and Decision-Making in Engineering**: The development and validation of instruments to assess critical thinking and decision-making compet...
- **Systems Thinking and Problem-Solving in Engineering**: The assessment of students' ability to approach complex engineering problems holistically, consideri...
- **Impact of Experiential Learning on Engineering Student Outcomes**: The exploration of how hands-on, real-world learning experiences such as internships, community-part...
- **Gender Differences in Engineering Competencies and Self-Efficacy**: The exploration of differences between male and female engineering students in terms of self-efficac...
- **Sustainability and Ethics Competencies in Engineering Education**: The integration of sustainability, ethics, and social responsibility into engineering curricula, and...
- **Innovation and Entrepreneurship Competencies in Engineering**: The measurement and development of innovation self-efficacy and entrepreneurial competencies among e...
- **Measurement Invariance and Fairness in Engineering Education Assessments**: The examination of whether assessment instruments function similarly across different subpopulations...
- **Metacognitive and Learning Orientation Tools in Engineering Education**: The creation and validation of tools designed to measure metacognitive skills, learning orientations...
- **Statistical Mediation and Correlation in Engineering Education Research**: The application of statistical methods such as mediation analysis and correlation to explore and exp...

---

## Methodology

This report implements **LLM triangulation** for bibliometric credibility.
Two independent LLMs classify the same data, and inter-coder reliability (ICR)
metrics are computed to emulate standard qualitative research practices.

### Phase 4b Metrics

- **Cohen's Kappa**: Chance-corrected agreement measure for categorical data
- **Confusion matrices**: Cross-tabulation of classifications by both models
- **% Agreement**: Proportion of citations where both dimensions match

### Phase 2e Metrics

- **Jaccard similarity**: Word-level overlap between theme names/definitions
- **Greedy matching**: 1:1 theme pairing by combined name+definition similarity
- **Subtopic overlap**: Jaccard of normalized subtopic sets
- **Grounding scores**: Hallucination control scores side by side

### References

- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement
  for categorical data. *Biometrics*, 33(1), 159-174.
- Cohen, J. (1960). A coefficient of agreement for nominal scales.
  *Educational and Psychological Measurement*, 20(1), 37-46.