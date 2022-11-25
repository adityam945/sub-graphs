
from SCC import *
from network import *

inp = [(0, 2), (0, 3), (0, 5), (1, 3), (1, 5), (2, 1), (2, 4), (2, 5), (3, 2), (3, 4), (4, 1), (4, 5), (5, 0), (5, 4)]

test = SCCManager(inp)
print(test.get_scc())
from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx
import matplotlib.pyplot as plt
n = 10
p = 0.5
g = erdos_renyi_graph(n, p, directed=False)
print(g.nodes)

G = g
test = graph_partitioning(G)