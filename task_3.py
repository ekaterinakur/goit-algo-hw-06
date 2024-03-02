import networkx as nx
import matplotlib.pyplot as plt
from kharkiv_metro_data import stations, connections_weighted

def dijkstra_algorithm(graph, source):
    distances = { node: float('infinity') for node in graph.nodes }
    distances[source] = 0
    visited = set()

    while len(visited) < len(graph.nodes):
        current_node = min((node for node in graph.nodes if node not in visited), key=lambda x: distances[x])
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph.get_edge_data(current_node, neighbor).get('weight', 1)
            potential_distance = distances[current_node] + weight

            if potential_distance < distances[neighbor]:
                distances[neighbor] = potential_distance

    return distances

if __name__ == "__main__":
    metro_network_weighted = nx.DiGraph()

    metro_network_weighted.add_nodes_from(stations)
    metro_network_weighted.add_weighted_edges_from(connections_weighted)

    # Знаходження найкоротших шляхів від кожної вершини до усіх інших за допомогою алгоритму Дейкстри
    for station in stations:
        shortest_paths = dijkstra_algorithm(metro_network_weighted, station)
        print(f"\nНайкоротший шлях від {station}: {shortest_paths}\n")
