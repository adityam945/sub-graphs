import networkx as nx
import matplotlib.pyplot as plt


def graph_partitioning(G, plotting=True):
    """Partition a directed graph into a list of subgraphs that contain
    only entirely supported or entirely unsupported nodes.
    """
    # Categorize nodes by their node_type attribute
    supported_nodes = {n for n, d in G.nodes(data="node_type") if d == "supported"}
    unsupported_nodes = {n for n, d in G.nodes(data="node_type") if d == "unsupported"}

    # Make a copy of the graph.
    H = G.copy()
    # Remove all edges connecting supported and unsupported nodes.
    H.remove_edges_from(
        (n, nbr, d)
        for n, nbrs in G.adj.items()
        if n in supported_nodes
        for nbr, d in nbrs.items()
        if nbr in unsupported_nodes
    )
    H.remove_edges_from(
        (n, nbr, d)
        for n, nbrs in G.adj.items()
        if n in unsupported_nodes
        for nbr, d in nbrs.items()
        if nbr in supported_nodes
    )

    # Collect all removed edges for reconstruction.
    G_minus_H = nx.DiGraph()
    G_minus_H.add_edges_from(set(G.edges) - set(H.edges))

    if plotting:
        # Plot the stripped graph with the edges removed.
        _node_colors = [c for _, c in H.nodes(data="node_color")]
        _pos = nx.spring_layout(H)
        plt.figure(figsize=(8, 8))
        nx.draw_networkx_edges(H, _pos, alpha=0.3, edge_color="k")
        nx.draw_networkx_nodes(H, _pos, node_color=_node_colors)
        nx.draw_networkx_labels(H, _pos, font_size=14)
        plt.axis("off")
        plt.title("The stripped graph with the edges removed.")
        plt.show()
        # Plot the the edges removed.
        _pos = nx.spring_layout(G_minus_H)
        plt.figure(figsize=(8, 8))
        ncl = [G.nodes[n]["node_color"] for n in G_minus_H.nodes]
        nx.draw_networkx_edges(G_minus_H, _pos, alpha=0.3, edge_color="k")
        nx.draw_networkx_nodes(G_minus_H, _pos, node_color=ncl)
        nx.draw_networkx_labels(G_minus_H, _pos, font_size=14)
        plt.axis("off")
        plt.title("The removed edges.")
        plt.show()

    # Find the connected components in the stripped undirected graph.
    # And use the sets, specifying the components, to partition
    # the original directed graph into a list of directed subgraphs
    # that contain only entirely supported or entirely unsupported nodes.
    subgraphs = [
        H.subgraph(c).copy() for c in nx.connected_components(H.to_undirected())
    ]

    return subgraphs, G_minus_H