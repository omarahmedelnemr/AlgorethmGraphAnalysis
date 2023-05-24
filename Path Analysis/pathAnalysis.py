import json
import networkx as nx
import matplotlib.pyplot as plt

# Load graph data from JSON file
with open('final.json', 'r') as file:
    graph_data = json.load(file)

# Create an empty graph
graph = nx.Graph()

# Add nodes and edges to the graph based on the JSON data
for data in graph_data:
    author_id = data['autherID']
    trend = data['trend']
    graph.add_node(author_id)
    graph.add_node(trend)
    graph.add_edge(author_id, trend)

source_node ='@EgyIndependent' # Specify the source node for path analysis
target_node = "@TourismandAntiq"  # Specify the target node for path analysis
try:
    path = nx.shortest_path(graph, source=source_node, target=target_node)
    # print(path)
    subGraph = nx.Graph()
    nodesList =[]
    colors = []
    print(path)
    pre = None
    for pathX in path: 
        subGraph.add_node(pathX)
        if pre!= None:
            subGraph.add_edge(pre,pathX)
        pre =pathX

    print(' -> '.join(path))
    nx.draw_networkx(subGraph,  with_labels=True)
    plt.title(f'Path Analysis Between Two Users.\n{source_node} -> {target_node}')
    plt.axis('off')
    plt.show()
    plt.savefig('Graph.png',format='PNG')

    
except nx.NetworkXNoPath:
    print('No paths found between the source and target nodes.')

