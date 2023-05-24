import json
import networkx as nx
import matplotlib.pyplot as plt

# Load JSON data from file
with open('final.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

# Create an empty graph
graph = nx.Graph()

# Add trend nodes to the graph
for item in data:
    trend = item['trend']
    graph.add_node(trend, color='yellow')

# Add author ID nodes and connect them to trends
for item in data:
    trend = item['trend']
    author_id = item['autherID']
    if author_id:
        graph.add_node(author_id, color='blue')
        graph.add_edge(author_id, trend)

# Calculate graph density
density = nx.density(graph)
print("Graph density:", density)

# Set node colors
node_colors = [data['color'] for _, data in graph.nodes(data=True)]

# Draw the graph
pos = nx.spring_layout(graph)  # Positions nodes using the Fruchterman-Reingold force-directed algorithm
nx.draw_networkx(graph, pos, with_labels=True, node_color=node_colors)

# Set plot options
plt.title('Network Graph')
plt.axis('off')

# Show the graph
plt.show()