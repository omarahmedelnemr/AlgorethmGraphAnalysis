import json
import networkx as nx

# Read data from the JSON file
with open("final.json", "r") as file:
    data = json.load(file)

# Create an empty graph
G = nx.Graph()

# Add nodes and edges to the graph based on the data
for item in data:
    trend = item["trend"]
    autherID = item["autherID"]
    G.add_node(trend)
    G.add_edge(trend, autherID)

# Calculate the clustering coefficient
clustering_coefficient = nx.average_clustering(G)

# Print the clustering coefficient
print("Clustering Coefficient:", clustering_coefficient)
