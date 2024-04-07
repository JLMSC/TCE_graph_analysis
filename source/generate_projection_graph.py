"""Generates a projection graph for bids and bidders from TCE."""
from typing import Any
import networkx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite


def generate_projection_graph(bipartite_graph: Any) -> None:
    """Creates a projection graph over bids.

    Creates a projection graph over a previously
    created bipartite graph.

    Parameters
    ----------
    bipartite_graph : Any
        Any previously created bipartite graph.
    """
    # Extract only bids node data from the bipartite graph.
    bids = {node for node, data in bipartite_graph.nodes(data=True) if data['is_bid'] == 1}

    # Creates a projection graph over 'bids' nodes from the bipartite graph.
    projection_graph = bipartite.projected_graph(B=bipartite_graph, nodes=bids, multigraph=True)

    # Draw and show the projection graph.
    networkx.draw(G=projection_graph, width=1, with_labels=True, font_size=6)
    plt.show()
