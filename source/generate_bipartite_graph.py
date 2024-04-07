"""Generates a bipartite graph for bids and bidders from TCE."""
from typing import Any
import networkx
import matplotlib.pyplot as plt


def generate_bipartite_graph(data: Any) -> Any:
    """Creates a bipartite graph for bids and bidders.

    Extract the data from a .json file, this should be
    collected from TCE, then creates a bipartite graph
    with both bids and bidders.

    Parameters
    ----------
    data : Any
        The TCE request data read from a .json file.

    Returns
    -------
    Any
        The bipartite graph created.
    """
    # Creates an empty graph.
    bipartite_graph = networkx.Graph()

    # Get bids and bidders as nodes.
    bidders, bids = [], []
    for content in data['data']:
        bids.append(content['numero_licitacao'])
        bidders.append(content['nome_negociante'])
    bipartite_graph.add_nodes_from(nodes_for_adding=bids, is_bid=1)
    bipartite_graph.add_nodes_from(nodes_for_adding=bidders, is_bid=0)

    # Create edges between those previous nodes.
    bipartite_connections = list(zip(bids, bidders))
    bipartite_graph.add_edges_from(ebunch_to_add=bipartite_connections)

    # Draw and show the bipartite graph.
    networkx.draw_networkx(
        G=bipartite_graph,
        pos=networkx.drawing.layout.bipartite_layout(G=bipartite_graph, nodes=bids),
        width=1,
        with_labels=True,
        font_size=6
    )
    plt.show()

    return bipartite_graph
