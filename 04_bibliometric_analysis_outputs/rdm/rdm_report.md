# Research Dynamics Manifold (RDM) — Report

## Formulation

Each article is mapped into a three-dimensional space [0,1]^3:

- **E (Emergence)**: Price Index (0.40) + Kleinberg Burst (0.35) + Keyword Novelty (0.25)
- **I (Impact)**: Sub-linear power mean (alpha=0.5) of MNCS, FWCI, citation velocity, social attention
- **S (Connectivity)**: Betweenness (0.30) + Interdisciplinarity (0.25) + Collaboration (0.20) + Sigma (0.25)

**RDM score** = ||r||_2 / sqrt(3) in [0,1]

## Descriptive Statistics

| Metric  | E | I | S | RDM |
|---------|---|---|---|-----|
| N       | 96 | 96 | 96 | 96 |
| Mean    | 0.500 | 0.472 | 0.500 | 0.506 |
| Median  | 0.527 | 0.470 | 0.500 | 0.491 |
| Std     | 0.133 | 0.194 | 0.162 | 0.110 |
| Min     | 0.239 | 0.226 | 0.175 | 0.215 |
| Max     | 0.690 | 0.844 | 0.866 | 0.804 |

## Archetype Distribution

| # | Archetype | N | % | Description |
|---|-----------|---|---|-------------|
| 1 | **Paradigm Shifters** | 18 | 18.8% | High emergence, high impact, well connected — the most dynamic articles |
| 2 | **Viral Novelties** | 11 | 11.5% | Novel and high-impact but structurally isolated — breakout papers |
| 3 | **Emerging Bridges** | 11 | 11.5% | Novel and well connected, future potential but not yet high impact |
| 4 | **Isolated Seeds** | 8 | 8.3% | Early or niche innovations — isolated seeds of future research |
| 5 | **Established Pillars** | 11 | 11.5% | Intellectual backbone — foundational works well integrated in the network |
| 6 | **Canonical Isolates** | 8 | 8.3% | Highly cited classics not centrally positioned in the knowledge network |
| 7 | **Silent Connectors** | 21 | 21.9% | Underestimated methodological bridges — low novelty and impact but structurally important |
| 8 | **Peripheral Works** | 8 | 8.3% | Routine contributions — low across all three dimensions |

## Top 15 Articles by RDM Score

| # | RDM | E | I | S | Archetype | Title |
|---|-----|---|---|---|-----------|-------|
| 1 | 0.804 | 0.690 | 0.844 | 0.866 | Paradigm Shifters | Measuring Undergraduate Students' Engineering Self-Efficacy: A Validat |
| 2 | 0.738 | 0.690 | 0.825 | 0.691 | Paradigm Shifters | Assessing students' motivation to engage in sustainable engineering. |
| 3 | 0.736 | 0.690 | 0.761 | 0.755 | Paradigm Shifters | Validity of the Contextual Competence Scale for Engineering Students. |
| 4 | 0.715 | 0.602 | 0.726 | 0.803 | Paradigm Shifters | The Employability Skills of Engineering Students': Assessment at the U |
| 5 | 0.712 | 0.642 | 0.741 | 0.748 | Paradigm Shifters | Innovation self-efficacy: A very brief measure for engineering student |
| 6 | 0.692 | 0.690 | 0.750 | 0.632 | Paradigm Shifters | Adapting Computer Programming Self-Efficacy Scale and Engineering Stud |
| 7 | 0.675 | 0.534 | 0.588 | 0.859 | Paradigm Shifters | Chemical engineering students' perceptions of peer and self-assessment |
| 8 | 0.660 | 0.579 | 0.754 | 0.635 | Paradigm Shifters | Prediction of Engineering Identity in Engineering Graduate Students. |
| 9 | 0.649 | 0.660 | 0.472 | 0.777 | Paradigm Shifters | Testing for measurement invariance in engineering identity constructs  |
| 10 | 0.645 | 0.545 | 0.837 | 0.500 | Paradigm Shifters | Education for Sustainable Development in Spanish engineering degrees.  |
| 11 | 0.643 | 0.598 | 0.771 | 0.537 | Paradigm Shifters | What Drives Engineering Students To Be Entrepreneurs? Evidence of Vali |
| 12 | 0.640 | 0.540 | 0.780 | 0.573 | Paradigm Shifters | Assessing reflective thinking in solving design problems: The developm |
| 13 | 0.639 | 0.461 | 0.614 | 0.797 | Established Pillars | Validation of the Internet entrepreneurial self-efficacy scale among R |
| 14 | 0.631 | 0.570 | 0.728 | 0.585 | Paradigm Shifters | Adaptation and validation of the Work Experience Questionnaire for inv |
| 15 | 0.623 | 0.353 | 0.572 | 0.844 | Established Pillars | Validation of Motivated Strategies for Learning Questionnaire: Compari |

## Top 5 per Archetype

### Paradigm Shifters (18 articles)

| RDM | E | I | S | Titulo |
|-----|---|---|---|--------|
| 0.804 | 0.690 | 0.844 | 0.866 | Measuring Undergraduate Students' Engineering Self-Efficacy: A Validat |
| 0.738 | 0.690 | 0.825 | 0.691 | Assessing students' motivation to engage in sustainable engineering. |
| 0.736 | 0.690 | 0.761 | 0.755 | Validity of the Contextual Competence Scale for Engineering Students. |
| 0.715 | 0.602 | 0.726 | 0.803 | The Employability Skills of Engineering Students': Assessment at the U |
| 0.712 | 0.642 | 0.741 | 0.748 | Innovation self-efficacy: A very brief measure for engineering student |

### Viral Novelties (11 articles)

| RDM | E | I | S | Titulo |
|-----|---|---|---|--------|
| 0.606 | 0.651 | 0.679 | 0.467 | A measure of affect toward key elements of engineering professional pr |
| 0.585 | 0.690 | 0.677 | 0.303 | Systems thinking skills of undergraduate engineering students |
| 0.576 | 0.559 | 0.735 | 0.377 | Engineering Students' Industrial Internship Experience Perception and  |
| 0.569 | 0.619 | 0.632 | 0.433 | Entrepreneurial Competences of University Students in the Digital Age: |
| 0.554 | 0.606 | 0.657 | 0.348 | Assessing students' IT professional values in a global project setting |

### Emerging Bridges (11 articles)

| RDM | E | I | S | Titulo |
|-----|---|---|---|--------|
| 0.560 | 0.690 | 0.343 | 0.591 | A Competency Model for Process Dynamics and Control and Its Use for Te |
| 0.539 | 0.585 | 0.452 | 0.570 | Compassion in Engineering Education: Validation of the Compassionate E |
| 0.523 | 0.623 | 0.427 | 0.500 | Examining Validity of General Self-Efficacy Scale for Assessing Engine |
| 0.502 | 0.645 | 0.299 | 0.500 | Evaluation Model of Student Competencies for Discussion Forums: An App |
| 0.491 | 0.651 | 0.226 | 0.500 | Do they understand your language? Assess their fluency with vector rep |

### Isolated Seeds (8 articles)

| RDM | E | I | S | Titulo |
|-----|---|---|---|--------|
| 0.488 | 0.668 | 0.419 | 0.303 | Identification and assessment of professional competencies for impleme |
| 0.481 | 0.534 | 0.438 | 0.467 | Transferable Skills in Engineering Curricula: A Case Study at a Portug |
| 0.466 | 0.626 | 0.396 | 0.319 | Development of a List of Can-do Statements for Global Communication in |
| 0.444 | 0.663 | 0.226 | 0.319 | Electricity performance measurement of engineering students by a Rasch |
| 0.443 | 0.552 | 0.427 | 0.319 | Validity of a Scale to Measure IC-PBL Learning Outcome in Engineering  |

### Established Pillars (11 articles)

| RDM | E | I | S | Titulo |
|-----|---|---|---|--------|
| 0.639 | 0.461 | 0.614 | 0.797 | Validation of the Internet entrepreneurial self-efficacy scale among R |
| 0.623 | 0.353 | 0.572 | 0.844 | Validation of Motivated Strategies for Learning Questionnaire: Compari |
| 0.612 | 0.443 | 0.595 | 0.758 | Development and initial validation of the Engineering Learning Experie |
| 0.606 | 0.478 | 0.773 | 0.526 | Development of a Scale for Measuring Students' Attitudes Towards Learn |
| 0.598 | 0.339 | 0.734 | 0.646 | Self-efficacy development in undergraduate engineering education |

### Canonical Isolates (8 articles)

| RDM | E | I | S | Titulo |
|-----|---|---|---|--------|
| 0.572 | 0.445 | 0.771 | 0.433 | Measuring the Programming Self-Efficacy of Electrical and Electronics  |
| 0.489 | 0.516 | 0.591 | 0.319 | Assessing vocational competencies in civil engineering: Lessons from A |
| 0.486 | 0.452 | 0.594 | 0.389 | Engineering Students' Perception on Self-Efficacy in Pre and Post Pand |
| 0.425 | 0.411 | 0.475 | 0.383 | ASSESSMENT OF GENERIC COMPETENCIES IN CIVIL ENGINEERING STUDENTS DURIN |
| 0.414 | 0.239 | 0.564 | 0.372 | Modifying the VALUE Rubrics to Assess the Entrepreneurial Mind-set |

### Silent Connectors (21 articles)

| RDM | E | I | S | Titulo |
|-----|---|---|---|--------|
| 0.569 | 0.508 | 0.451 | 0.714 | Development of a Questionnaire to Measure Students' Attitudes and Perc |
| 0.519 | 0.492 | 0.226 | 0.717 | WIP: Confirmatory Factor Analysis of Instruments to Measure Connection |
| 0.506 | 0.363 | 0.226 | 0.766 | Understanding student motivation and self-efficacy in differential cal |
| 0.494 | 0.516 | 0.396 | 0.557 | Measuring Employability Skills of Budding IT Professionals in India |
| 0.477 | 0.407 | 0.226 | 0.684 | Modeling the integration of ethics, social responsibility, and sustain |

### Peripheral Works (8 articles)

| RDM | E | I | S | Titulo |
|-----|---|---|---|--------|
| 0.431 | 0.453 | 0.386 | 0.451 | Validation of the Academic Analogue of Psychological Momentum Theory o |
| 0.410 | 0.453 | 0.468 | 0.282 | Self-perception on the Acquisition of Investigative Competencies in th |
| 0.392 | 0.420 | 0.226 | 0.483 | Do transferable skills matter for engineering students? |
| 0.338 | 0.425 | 0.243 | 0.321 | Items for Measuring the Construct of Workplace Oral Communication Skil |
| 0.331 | 0.239 | 0.437 | 0.282 | Exploring the relationships between resilience and student performance |

## Mathematical Justification

### Rank Normalization (Empirical CDF)
Each sub-indicator x is transformed to its percentile F(x) = P(X <= x).
This guarantees scale invariance and comparability across corpora of different sizes.

### Sub-linear Power Mean (alpha = 0.5)
The I axis uses a generalized power mean:
```
M_{0.5}(x_1,...,x_K) = [ (1/K) * sum(x_j^{0.5}) ]^{2}
```
Key property: penalizes imbalance across diffusion channels.
An article with high impact in a single channel (e.g., only citations,
no social attention) scores lower than one with moderate impact across
multiple channels. This captures the notion of 'broad diffusion'.

### Axis Orthogonality
- E (temporal novelty) vs I (accumulated citations): correlation ~0
  in the literature (new articles have not had time to accumulate citations).
- E vs S (network centrality): independent (novelty does not imply central position).
- I vs S: weak correlation (~0.2-0.3 typical); rank normalization
  minimizes residual dependence.

### RDM Scalar Score
```
RDM_i = ||r_i||_2 / sqrt(3) = sqrt(E^2 + I^2 + S^2) / sqrt(3)
```
Range [0,1]. Articles at the corner (1,1,1) achieve RDM=1.
Division by sqrt(3) normalizes the unit cube diagonal.

### Octant Classification
Corpus medians define the cutting planes, creating an
empirically adaptive taxonomy (no fixed thresholds).
Each octant corresponds to an interpretable archetype.
