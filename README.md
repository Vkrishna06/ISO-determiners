# ISO-determiners

Project Title: ISO Determiners - Semi-automated determination system for illicit synthetic opioid tracking

This project aims to provide regulatory bodies and law enforcement with an evidence-based, transparent, and tunable platform to rank entities involved in synthetic opioid (ISO) supply chains, using a combination of NLP, manual tagging, and a weighted risk model.

Team Members:

- Bhargav Dasari
- Sagarika Komati Reddy
- Venkata Krishna Kothapalli
- Kamani Madasu
- Uday Madivada
- Suparna Mannava 

Overview:

The ISO Determination Engine is a semi-automated system designed to detect and prioritize risks related to illicit synthetic opioid (ISO) activities. Built by the Team ISO Determiners as part of the Spring 2025 capstone project at George Mason University (DAEN-690), this tool focuses on ranking high-risk companies and fentanyl precursor chemicals using a weighted scoring model informed by real-world evidence.

Problem Statement:

The opioid crisis, particularly involving fentanyl and its precursors, continues to devastate public health systems, with over 70,000 annual overdose deaths in the U.S. alone. A significant portion of fentanyl trafficking is enabled by legal businesses that mask illicit chemical redirection. Current tools lack automation, evidence traceability, and risk prioritization capabilities.


Solution Approach:

The ISO Determination Engine is a semi-automated system that combines natural language processing (NLP), entity recognition, manual tagging, and risk scoring to evaluate the potential complicity of companies and chemicals involved in fentanyl production.

The system is structured as a modular pipeline:

1. Document Ingestion - Intake of press releases, sanction lists, court records
2. Entity Recognition - Extraction of chemical names and company aliases
3. Evidence Tagging - Manual and NLP-assisted tagging of key phrases
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
| Fentanyl Precursors Table | Academic/DEA |               CAS numbers, synonyms, weights                |


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
- Evidence Tagging - Manual/NLP-assisted tagging of sanctions, subsidies, and complicity evidence.
- Entity Recognition - NLP pipeline for extracting companies and chemical names.
- Interactive Dashboard - View and adjust risk scores, export results, and filter by tags.
- Clustering Analysis - K-means clustering to identify hidden networks.


Project Timeline:


| Sprint |            Objectives           |   Status   |
|--------|---------------------------------|------------|
|    1   | Define scope, collect datasets  |  Completed |
|    2   | Build risk model, design schema |  Completed |
|    3   |    Develop UI, integrate NLP    |  Completed |
|    4   |  Testing, feedback, validation  |  Completed |
|    5   | Finalize documentation & report |   Ongoing  |



## References

- [Select Committee on the CCP](https://selectcommitteeontheccp.house.gov/)
- [TraCCC Research](https://traccc.gmu.edu/)
- [CDC Report on Fentanyl](https://blogs.cdc.gov/nchs/2023/05/03/7338/)




