import networkx as nx
import matplotlib.pyplot as plt
from kharkiv_metro_data import stations, connections

metro_network = nx.DiGraph()

metro_network.add_nodes_from(stations)
metro_network.add_edges_from(connections)

def print_main_characteristics(graph):
    num_vertices = graph.number_of_nodes()
    num_edges = graph.number_of_edges()

    print("\nХарактеристики:\n")
    print(f"{'Кількість вершин':<22}: {num_vertices}")
    print(f"{'Кількість звєязків':<22}: {num_edges}")

    degrees = graph.degree()
    print("\nСтупені вершин:\n")
    for station, degree in degrees:
        print(f"{station:<22}: {degree}")
    print("\n")

def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(
        graph,
        pos,
        with_labels=True,
        font_weight='bold',
        node_size=1000,
        node_color='orange',
        edge_color='violet',
        font_size=8,
        arrowsize=20
    )
    plt.title('Схема метро м. Харків')
    plt.show()

if __name__ == "__main__":
    print_main_characteristics(metro_network)
    visualize_graph(metro_network)
