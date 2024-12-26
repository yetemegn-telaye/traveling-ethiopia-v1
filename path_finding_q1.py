from collections import deque
import heapq
from graph_representation_q1 import draw_graph_with_path


def uninformed_path_finder(cities, roads, start_city, goal_city, strategy, weighted=False):
    if strategy not in ['bfs', 'dfs']:
        raise ValueError("Strategy must be 'bfs' or 'dfs'")

    if strategy == 'bfs':
        if weighted:
            frontier = [(0, start_city, [start_city])]
            heapq.heapify(frontier)

        else:
            frontier = deque([(start_city, [start_city], 0)])
        
        visited = set()  

        while frontier:
            if weighted:
                cost, current_city, path = heapq.heappop(frontier)

            else:    
                current_city, path, cost = frontier.popleft()
          
            if current_city == goal_city:
                return path, cost

            if current_city not in visited:
                visited.add(current_city)

                
                for neighbor, distance in roads.get(current_city, []):
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        new_cost = cost + (distance if weighted else 1)
                        if weighted:
                            heapq.heappush(frontier, (new_cost, neighbor, new_path))
                        else:
                            frontier.append((neighbor, new_path, new_cost))

    
    elif strategy == 'dfs':
       
        frontier = [(start_city, [start_city], 0)]  
        visited = set()

        while frontier:
            
            current_city, path, cost = frontier.pop()

            
            if current_city == goal_city:
                return path, cost

           
            if current_city not in visited:
                visited.add(current_city)

                
                for neighbor, distance in roads.get(current_city, []):
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        new_cost = cost + distance
                        frontier.append((neighbor, new_path, new_cost))

    
    return None, float('inf')

cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}


path, cost = uninformed_path_finder(cities, roads, 'Addis Ababa', 'Mekelle', 'bfs',weighted=False)
draw_graph_with_path(cities, roads, path, cost)
print(path, cost)


# path, cost = uninformed_path_finder(cities, roads, 'Addis Ababa', 'Mekelle', 'dfs',weighted=False)
# draw_graph_with_path(cities, roads, path, cost)
# print(path, cost)