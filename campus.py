import networkx as nx 
import matplotlib.pyplot as plt

campus_coordinates = {

    "A": (9, 5),
    "B": (7, 0),
    "C": (5, 5),
    "D": (3, 0),
    "E": (1, 5),
    "F": (3, 10),
    "G": (1, 15),
    "H": (3, 20),
    "I": (5, 15),
    "J": (7, 20),
    "K": (9, 15),
    "L": (7, 10),
    "M": (3, 35),
    "N": (1, 33),
    "W": (6, 30)
}
g = nx.Graph()
g.add_nodes_from(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","W"])

g.add_edge("A","L")
g.add_edge("C","L")
g.add_edge("K","L")
g.add_edge("I","L")
g.add_edge("C","B")
g.add_edge("C","D")
g.add_edge("C","F")
g.add_edge("D","E")
g.add_edge("F","G")
g.add_edge("I","H")
g.add_edge("I","J")
g.add_edge("I","W")
g.add_edge("M","N")
g.add_edge("M","W")

def draw_map_with_path(graph, coordinates, path=None):
    plt.figure(figsize=(8, 10))

    # Draw full campus
    nx.draw(
        graph,
        pos=coordinates,
        with_labels=True,
        node_color="red",
        node_size=2500,
        font_size=14,
        font_color="white",
        font_weight="bold",
        width=3
    )

    # Highlight path
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            graph,
            pos=coordinates,
            edgelist=path_edges,
            edge_color="green",
            width=6
        )

        nx.draw_networkx_nodes(
            graph,
            pos=coordinates,
            nodelist=path,
            node_color="green",
            node_size=3000
        )

    plt.show()
