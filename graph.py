import json
import networkx as nx
import matplotlib.pyplot as plt
import pickle


# Load JSON data from file
with open('real.json', 'r') as file:
# with open('final.json', 'r') as file:
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

# Set node colors
node_colors = [data['color'] for _, data in graph.nodes(data=True)]

# Draw the graph
nx.draw_networkx(graph,  with_labels=True, node_color=node_colors)

# Set plot options
plt.title('Twitter users-trends Interactions')
plt.axis('off')
# Save the Figure
plt.savefig('Graph.png',format='PNG')
plt.savefig('Graph.svg',format='SVG')

figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()

# Show the graph
plt.show()


# save graph object to file
pickle.dump(graph, open('final.graph', 'wb'))