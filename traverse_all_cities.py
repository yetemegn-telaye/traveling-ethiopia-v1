import networkx as nx
from collections import deque
import matplotlib.pyplot as plt
from time import sleep

def traverse_all_cities(cities, roads, start_city, strategy):
 
    visited = set()
    path = []
    total_cost = 0

    frontier = deque([(start_city, [], 0)]) if strategy == 'bfs' else [(start_city, [], 0)]  # (current_city, path_so_far, cost_so_far)

    while frontier:
        current_city, current_path, cost_so_far = (
            frontier.popleft() if strategy == 'bfs' else frontier.pop()
        )

        if current_city in visited:
            continue

       
        visited.add(current_city)
        current_path = current_path + [current_city]

       
        path = current_path
        total_cost = cost_so_far

       
        for neighbor, distance in roads.get(current_city, []):
            if neighbor not in visited:
                frontier.append((neighbor, current_path, cost_so_far + distance))

    return path, total_cost


def visualize_graph_with_agent(cities, roads, path, cost):
    G = nx.Graph()
    
   
    for city in cities:
        G.add_node(city)
    for city, neighbors in roads.items():
        for neighbor, distance in neighbors:
            G.add_edge(city, neighbor, weight=distance)

  
    pos = nx.spring_layout(G)

   
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 8))

    for i in range(len(path)):
        ax.clear() 
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, ax=ax)
        nx.draw_networkx_edges(G, pos, edge_color="gray", ax=ax)

       
        nx.draw_networkx_nodes(G, pos, nodelist=path[:i + 1], node_color="orange", ax=ax)

        
        nx.draw_networkx_nodes(G, pos, nodelist=[path[i]], node_color="red", ax=ax)

        ax.set_title(f"Agent's Traversal (Step {i + 1}/{len(path)})\nTotal Cost So Far: {sum([roads[path[j]][0][1] for j in range(i)] if i > 0 else [0])}")
        plt.pause(1) 

   
    plt.ioff()
    plt.show()

    print(f"Final Path: {path}")
    print(f"Total Cost: {cost}")



cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}


strategy = 'bfs'
start_city = 'Addis Ababa'


path, cost = traverse_all_cities(cities, roads, start_city, strategy)


print(f"BFS Path: {path} with cost {cost}")

