# from networkx.generators.random_graphs import erdos_renyi_graph
# import networkx as nx
# import matplotlib.pyplot as plt
# n = 6
# p = 0.5
# g = erdos_renyi_graph(n, p, directed=True)
# print(g.nodes)
# # [0, 1, 2, 3, 4, 5]
# print(g.edges)
# # [(0, 1), (0, 2), (0, 4), (1, 2), (1, 5), (3, 4), (4, 5)]

# # g.add_edges_from(g)
# nx.draw_networkx(g)
# plt.show()

# ahyahd

# import matplotlib.pyplot as plt
# import networkx as nx

# G = nx.Graph()

# G.add_edge("a", "b", weight=0.6)
# G.add_edge("a", "c", weight=0.2)
# G.add_edge("c", "d", weight=0.1)
# G.add_edge("c", "e", weight=0.7)
# G.add_edge("c", "f", weight=0.9)
# G.add_edge("a", "d", weight=0.3)

# elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
# esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

# pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# # nodes
# nx.draw_networkx_nodes(G, pos, node_size=700)

# # edges
# nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
# nx.draw_networkx_edges(
#     G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
# )

# # node labels
# nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# # edge weight labels
# edge_labels = nx.get_edge_attributes(G, "weight")
# nx.draw_networkx_edge_labels(G, pos, edge_labels)

# ax = plt.gca()
# ax.margins(0.08)
# plt.axis("off")
# plt.tight_layout()
# plt.show()

# import random
# num_nodes = 3
# nodelist = list(range(1, num_nodes + 1))
# print(nodelist)
# edgelist = []
# for i in nodelist:
#     for j in nodelist:
#         if j > i:
#             break
#         if i == j:
#             edgelist.append((i, j, 0))
#         else:
#             rand = random.randint(5, 25)
#             edgelist.append((i, j, rand))
#             edgelist.append((j, i, rand))
# print(edgelist)



from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx
import matplotlib.pyplot as plt
n = 6
p = 0.5
g = erdos_renyi_graph(n, p, directed=True)
print(g.nodes)

G = g

import random
# #code creating G here
# for (u,v,w) in G.edges(data=True):
#     w['weight'] = random.randint(0,10)

for (u, v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(0,10)


print(G.edges)
for (u, v, d) in G.edges(data=True):
    print(u, v, d)

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()

