import json
import networkx as nx
import community as community_louvain

# Load data from the JSON file
with open("final.json", "r") as file:
    data = json.load(file)

# Create an empty graph
G = nx.Graph()

# Add nodes and edges to the graph
for entry in data:
    trend = entry["trend"]
    author = entry["autherID"]
    G.add_edge(trend, author)

# Perform community detection using Louvain algorithm
partition = community_louvain.best_partition(G)
result = ''
# Print the detected communities
for community_id, nodes in partition.items():
    print(f"Community {community_id}: {nodes}")
    result +=f"Community {community_id}: {nodes}\n"

with open("CommDis.txt",'w') as file:
    file.write(result)
