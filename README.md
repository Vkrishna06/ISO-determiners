# ISO-determiners

1.Project Title: ISO Determiners - Semi-automated determination system for illicit synthetic opioid tracking

This project, developed as part of the DAEN-690 Capstone at George Mason University (Spring 2025), aims to provide regulatory agencies and law enforcement with a transparent, evidence-backed, and tunable platform to monitor and prioritize high-risk entities in the synthetic opioid (ISO) supply chain.

2.Team Members:

- Bhargav Dasari
- Sagarika Komati Reddy
- Venkata Krishna Kothapalli
- Suparna Mannava
- Uday Madivada
- Kamani Madasu 

3.Overview:

The ISO Determination Engine is a semi-automated framework that prioritizes entities involved in illicit synthetic opioid (ISO) activity. The system leverages structured evidence and risk scoring models to identify suspicious companies associated with fentanyl trafficking.

It helps investigators by providing:

- Easy-to-follow and adjustable risk scoring tools.
- A central place to tag supporting evidence.
- Tools to automatically find names of people, companies, and chemicals in text.
- Dashboards that show live updates and insights.

4.Problem Statement:

The opioid epidemic, driven largely by synthetic opioids like fentanyl, claims over 70,000 lives each year in the U.S. The fentanyl supply chain often operates under the guise of legitimate businesses—making it hard for enforcement agencies to distinguish illicit actors.

Existing tools lack:
- Automation
- Evidence traceability
- Configurable risk models

Our project addresses this by building a dynamic, data-driven system that adapts as new information becomes available.

5.Solution Approach:

The ISO Determination Engine is a semi-automated system that combines entity recognition, manual tagging, and risk scoring to evaluate the potential complicity of companies and chemicals involved in fentanyl production.

The system is structured as a modular pipeline:

1. Document Ingestion - Intake of press releases, sanction lists, court records
2. Entity Recognition - Extraction of chemical names and company aliases
3. Evidence Tagging - Manual tagging of key phrases
4. Scoring Model - Weighted scoring using configurable formulas
5. Interactive Dashboard - Dynamic view of scores, sources, and trends
6. Clustering Analysis - Unsupervised learning to find suspicious networks

This structured approach allows law enforcement and analysts to:
- Prioritize entities based on behavior-linked risk
- Adjust model weights to reflect enforcement needs
- Track every risk score back to supporting evidence


6.Datasets Used

|          Dataset          |    Source    |                       Description                           |
|---------------------------|--------------|-------------------------------------------------------------|
|        DOJ Indictments    |     USDOJ    | Press releases and case details of fentanyl-related charges |
|          DEA SSL          |      DEA     |           List of scheduled precursor chemicals             |
|  Company Reference Sheet  |    Curated   |     PRC-linked companies, aliases, sanctions, subsidies     |


7. Weighted Scoring Model

Risk Scoring Model

The total risk score for each company is calculated using:

Total Score = (Sanctions × 1.2) + (Subsidies × 1.1) + (Complicity × 1.3)

|    Component   |                    Description                    | Weight |
|----------------|---------------------------------------------------|--------|
|  Sanctions (S) |       Legal actions taken against the entity      |   1.2  |
|  Subsidies (G) | Government support potentially enabling ISO trade |   1.1  |
| Complicity (C) |      Behavioral or circumstantial involvement     |   1.3  |

Weights are configurable from the Streamlit UI.


8.Key Features:

- Risk Scoring Engine - Customizable and auditable scoring for each entity.
- Evidence Tagging - Manual tagging of sanctions, subsidies, and complicity evidence.
- Entity Recognition - NLP pipeline for extracting companies and chemical names.
- Interactive Dashboard - View and adjust risk scores, export results, and filter by tags.
- Clustering Analysis - K-means clustering to identify hidden networks.


9.Project Timeline:


| Sprint |            Objectives           |   Status   |
|--------|---------------------------------|------------|
|    1   | Define scope, collect datasets  |  Completed |
|    2   | Build risk model, design schema |  Completed |
|    3   |           Develop UI            |  Completed |
|    4   |  Testing, feedback, validation  |  Completed |
|    5   | Finalize documentation & report |  Completed |

10.Limitations & Future Work

- Manual tagging remains labor-intensive. Future versions could enhance NLP confidence thresholds and pre-training.
- OCR tools like AWS Textract have limitations on PDF formatting—improving these pipelines is key.
- Future versions could automate tagging pipelines, integrate real-time court record scraping, and increase dashboard interactivity.


References

- [Select Committee on the CCP](https://selectcommitteeontheccp.house.gov/)
- [TraCCC Research](https://traccc.gmu.edu/)
- [CDC Report on Fentanyl](https://blogs.cdc.gov/nchs/2023/05/03/7338/)




