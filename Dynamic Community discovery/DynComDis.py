import networkx as nx
import community
import json

# Load the data from the original JSON file
with open('final.json', 'r') as infile:
    data = json.load(infile)

# Extract the unique trend names and assign IDs to them
trends = list(set(d['trend'] for d in data))
trend_ids = {trend: i+1 for i, trend in enumerate(trends)}

# Print the trend names and their corresponding IDs
for trend in trend_ids:
    print(f"{trend}: {trend_ids[trend]}")

# Create a list of nodes
nodes = [{'id': i} for i in range(1, len(trends)+1)]

# Create a list of edges based on author IDs and their corresponding trend IDs
edges = []
for d in data:
    source = d['autherID']
    target = trend_ids[d['trend']]
    edges.append({'source': source, 'target': target})

# Create a dictionary with the 'nodes' and 'edges' fields
graph = {'nodes': nodes, 'edges': edges}

# Save the graph as a JSON file with indentation and multiple lines
json_string = json.dumps(graph, indent=4)
data = json.loads(json_string)

# Create a networkx graph
G = nx.Graph()

# Add nodes to the graph
for node in data['nodes']:
    G.add_node(node['id'])

# Add edges to the graph
for edge in data['edges']:
    G.add_edge(edge['source'], edge['target'])

# Detect communities using the Louvain method
partition = community.best_partition(G)

# Create a dictionary of communities
communities = {}
for node, com_id in partition.items():
    if com_id not in communities:
        communities[com_id] = []
    communities[com_id].append(node)

# Format the communities as a list of lists
community_list = [nodes for nodes in communities.values()]

# Save the partition as a JSON file with indentation and multiple lines
with open('abbas.json', 'w') as outfile:
    json.dump(community_list, outfile, indent=4)
    
    
    
    
    
    
    
    
