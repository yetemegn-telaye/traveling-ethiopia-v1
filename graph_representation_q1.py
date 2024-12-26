import networkx as nx
import matplotlib.pyplot as plt
from PyQt5.QtGui import QRawFont

def draw_graph_with_path(cities,roads, path=None, cost=None):
    G = nx.MultiGraph()
    G.add_nodes_from(cities)
    for city in cities:
        for road in roads[city]:
            G.add_edge(city, road[0], weight=road[1])
            
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color='green',
        font_size=7,
        font_color='white',
        font_weight='bold'
    )
    for (u, v, key, data) in G.edges(data=True, keys=True):
        label = data['weight']
        x = (pos[u][0] + pos[v][0]) / 2
        y = (pos[u][1] + pos[v][1]) / 2
        plt.text(x, y, str(label), fontsize=8, color='red', ha='center')

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=path_edges,
            edge_color='red',
            width=3
        )
        plt.title(f"Path Found: {path} Cost: {cost}")
    plt.show()

cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

path = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Mekelle']
cost = 510 + 180 + 300

# draw_graph_with_path(cities, roads, path, cost)