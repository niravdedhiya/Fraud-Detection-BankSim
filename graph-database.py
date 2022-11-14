import json
from py2neo import Graph

fraud_graph = Graph(password="Fraud_Banksim", bolt_port=7687, http_port=7474)

query = """MATCH (p:Placeholder)
RETURN p.id AS id, p.degree AS degree, p.pagerank as pagerank, p.community aS community 
"""

data = fraud_graph.run(query)

with open("data/graph_features.json", "w") as file:
    json.dump(data, file)

