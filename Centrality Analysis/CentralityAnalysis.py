import json
import networkx as nx

# Load the JSON file into a Python object
with open('final.json', 'r') as f:
    data = json.load(f)

# Create an empty dictionary to hold the graph data
graph = {}

# Loop through the edges in the input data and add them to the graph dictionary
for edge in data:
    source, target = edge['autherID'], edge['trend']
    if source not in graph:
        graph[source] = []
    graph[source].append(target)

# Convert the graph dictionary to a JSON string
json_string = json.dumps(graph, indent=2)
data = json.loads(json_string)

#################

# Loop through each key-value pair in the dictionary
for key, value in data.items():
    # Remove duplicates from the array
    data[key] = list(set(value))

###################

# Create a NetworkX graph object from the data
graph = nx.from_dict_of_lists(data)

# Compute the centrality measures for the nodes in the graph
degree_centrality = nx.degree_centrality(graph)
betweenness_centrality = nx.betweenness_centrality(graph)
closeness_centrality = nx.closeness_centrality(graph)
eigenvector_centrality = nx.eigenvector_centrality_numpy(graph)

# Print the centrality measures for each node in the graph
k = ''
for node in graph.nodes:
    degree = degree_centrality[node]
    betweenness = betweenness_centrality[node]
    closeness = closeness_centrality[node]
    eigenvector = eigenvector_centrality[node]
    k = k + (f"Node {node} has degree centrality of {degree}, betweenness centrality of {betweenness}, closeness centrality of {closeness}, and eigenvector centrality of {eigenvector} \n - \n")

# Write the output to a file
with open("nonononono.txt", "w", encoding="utf-8") as f:
    f.write(k)
    
    
    