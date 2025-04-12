# ISO-determiners

Project Title: ISO Determiners – Automating Illicit Activity Detection

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

Fentanyl trafficking has become a critical issue, contributing to over 70,000 overdose deaths annually in the U.S. The global fentanyl supply chain operates through legal businesses that often redirect chemicals into illicit markets. Current tracking methods lack automation, creating inefficiencies in intelligence gathering and risk assessment.

This project addresses the need for a data-driven approach to identifying and prioritizing high-risk companies and chemicals linked to fentanyl production. By implementing a structured, analytical framework, law enforcement can more effectively disrupt illicit supply networks.


Solution Approach:

The project develops a semi-automated risk assessment system that:
- Uses structured intelligence to log and trace key events (e.g., sanctions, indictments, and financial crimes).
- Implements a weighted scoring model to assess the risk level of entities based on various indicators.
- Provides interactive visualizations and dashboards for regulatory agencies to monitor illicit activities.
- Integrates supervised machine learning and anomaly detection to flag suspicious transactions.
- Enhances data collection through NLP-based entity recognition to extract information from legal reports and sanctions lists.

Key Features:

Weighted Risk Scoring Engine
Calculates total risk scores for chemical-company pairs using a configurable formula:
Total Score = (Sanctions × w1) + (Subsidies × w2) + (Complicity × w3)

Default weights:

Sanctions (w1) = 1.2
Government Subsidies (w2) = 1.1
Complicity Indicators (w3) = 1.3

Manual Tagging Interface:
Allows manual tagging and classification of evidence related to company behavior, government funding, and legal violations.

Evidence Traceability:
Every risk score is backed by evidence from DOJ press releases, OFAC sanctions, PACER court records, and DEA databases.

Interactive Dashboard (Streamlit):
- Displays risk scores and entity breakdowns  
- Allows dynamic adjustment of scoring weights**  
- Supports search, filtering, and export options

Clustering Analysis:
K-means unsupervised models detect hidden networks or suspicious clusters of fentanyl suppliers.

System Architecture:

Data Sources ➜ Intake Log ➜ NLP/Tagging ➜ Sub-score Assignment ➜ Weighted Scoring ➜ Dashboard Output

- Evidence Collection: From DOJ, OFAC, DEA, CBP, PACER
- Pipeline: Identifies and extracts entity names (chemicals/companies)
- Scoring Engine: Assigns scores and ranks risk levels
- Dashboard: Filter, compare, and export outputs

Datasets Used:

- USDOJ Fentanyl Precursor Indictments
Court filings, case numbers, indictment press releases

- DEA Special Surveillance List (SSL)
List of precursor chemicals relevant to fentanyl production

- Integrated Company Reference Sheet
Company aliases, PRC-linked funding, risk indicators

- Fentanyl Precursors Chemical Table
CAS numbers, synonyms, substance weights

Risk Scoring Model:

The weighted scoring model assesses risk based on three key factors:

- Sanctions & Indictments (S): Legal actions taken against a company.
- Government Subsidies (G): Financial support or policies aiding illicit activities.
- Complicity Indicators (C): Business behaviors that suggest involvement in illegal supply chains.

  These are scored and combined using:
Total Score = (S × 1.2) + (G × 1.1) + (C × 1.3)

Key Findings:

- Majority of flagged companies are based in China and Mexico.
- Complicity indicators were stronger predictors than sanctions alone.
- The model is flexible and tunable, allowing adjustments for different enforcement priorities.
- Manual tagging ensures high precision**, critical for sensitive topics.
- All scores are backed by evidence, enhancing auditability and trust.

Project Timeline:

- Sprint 1 -- Define project scope & collect initial datasets --  Completed
- Sprint 2 -- Develop risk scoring algorithm & refine data structures -- Completed
- Sprint 3 -- Implement UI prototype & integrate NLP tools -- Completed
- Sprint 4 -- Final testing, validation, and partner feedback -- Upcoming
- Sprint 5 -- Complete documentation and submit findings -- Pending


References:
- Select Committee on the CCP: https://selectcommitteeontheccp.house.gov/
- TraCCC Research: https://traccc.gmu.edu/
- CDC Reports on Fentanyl: https://blogs.cdc.gov/nchs/2023/05/03/7338/



