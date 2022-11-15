# Fraud-Detection-BankSim
Fraud Detection using Graph Databases and Machine Learning on the BankSim Dataset

## Folder Structure

    Fraud-Detection-BankSim
    .
    │
    ├── analysis and results
    │   ├── banksim.html
    │   ├── experiments_vis.pdf
    │
    │
    ├── data
    │   ├── bs140513_032310.csv
    │   ├── bsNET140513_032310.csv
    │   ├── graph_features.json 
    │
    │
    ├── fraud-detection-base.ipynb 
    ├── fraud-detection-main.ipynb
    ├── graph-database.py
    ├── graphdb_creation.cyp
    ├── README.md
    
## File Description

<ul> 
  <li><b>banksim.html</b> - Exploratory Data Analysis for the BankSim Dataset.</li>
  <li><b>experiments_vis.pdf</b> - Contains final results and their screenshots.</li>
  <li><b>bs140513_032310.csv</b> - Main file which contains the transactional data.</li>
  <li><b>bsNET140513_032310.csv</b> - Contains information about graph attributes.</li>
  <li><b>graph_features.json</b> - JSON data file that contains data extracted data from Neo4j graph.</li>
  <li><b>fraud-detection-base.ipynb</b> - Contains code implementation which doesn't handle the class imbalance problem.</li>
  <li><b>fraud-detection-main.ipynb</b> - Final file which contains code implementation that handles class imbalance problem.</li>
  <li><b>graph-database.py</b> - File which extracts required features from the Neo4j graph and dumps them into a JSON file.</li>
  <li><b>graphdb_creation.cyp</b> - Cypher query file that creates the Neo4j graph.</li>
  <li><b>README.md</b> - File explaining this GitHub repository's folder structure and contains description for each file.</li>
</ul>  
    
