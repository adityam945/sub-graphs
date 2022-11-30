from networkx import edge_subgraph
def subb(G):
    H = G.edge_subgraph([(0, 1), (3, 4)])
    