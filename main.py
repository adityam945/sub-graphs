
from SCC import *
from network import *
import time
start = time.time()
# inp = [(0, 2), (0, 5), (1, 2), (1, 3), (2, 1), (3, 0), (3, 1), (3, 2), (4, 3), (4, 5), (5, 1), (5, 3), (5, 4)]
# test = SCCManager(inp)
# clusters = test.get_scc()
# for i in clusters:
#     print(i)

# for u,v in inp:
#     print(u,v)
# from lxml import etree

file1 = open('some.txt', 'r')
Lines = file1.readlines()
import re


graph = []

file = 'some.txt'
f=open(file,"r")
lines=f.readlines()
result1=[]
result2=[]
result3=[]

for x in lines:
    result1.append(x.split(' ')[0])
    result2.append(x.split(' ')[1])
    result3.append(x.split(' ')[2])
f.close()


# print(result1)
res = [ (
    (result1[i]), (result2[i]) )
        for i in range(len(result1))]

resWeighted = [ (
    (result1[i]), (result2[i]), (result3[i][:-1]))
        for i in range(len(result1))]

graphPoint = res
print('started SCC')
result1_unique = [*set(result1)]
G = nx.path_graph(graphPoint) 



# node_degree_dict=nx.degree(G)
G2= G.subgraph(result1_unique)

print(G2)
print(G2.edges)

import json

with open('outfile.txt', 'w') as file:
    # file.writelines('\t'.join(str(j) for j in i) + '\n' for i in G2)
    file.writelines('\n'.join(str(i)) for i in G2)


with open('outt.txt', 'w') as f:
    f.write(json.dumps(G2))
with open('outt2.txt', 'w') as f:
    f.write(json.dumps(G))

# import networkx as nx
# from collections import defaultdict
# from itertools import combinations
# from dwave.system.samplers import DWaveSampler
# from dwave.system.composites import EmbeddingComposite
# import math

# # ------- Set tunable parameters -------
# num_reads = 1000
# gamma = 80
# print("Graph on {} nodes created with {} out of {} possible edges.".format(len(G.nodes), len(G.edges), len(G.nodes) * (len(G.nodes)-1) / 2))

# # Initialize our Q matrix
# Q = defaultdict(int)

# # Fill in Q matrix
# for u, v in G.edges:
#     Q[(u,u)] += 1
#     Q[(v,v)] += 1
#     Q[(u,v)] += -2

# for i in G.nodes:
#     Q[(i,i)] += gamma*(1-len(G.nodes))

# for i, j in combinations(G.nodes, 2):
# 	Q[(i,j)] += 2*gamma

# # ------- Run our QUBO on the QPU -------

# # Set chain strength
# chain_strength = gamma*len(G.nodes)

# # Run the QUBO on the solver from your config file
# sampler = EmbeddingComposite(DWaveSampler())
# response = sampler.sample_qubo(Q,
#                                chain_strength=chain_strength,
#                                num_reads=num_reads,
#                                label='Example - Graph Partitioning')

# # See if the best solution found is feasible, and if so print the number of cut edges.
# sample = response.record.sample[0]

# # In the case when n is odd, the set may have one more or one fewer nodes
# if sum(sample) in [math.floor(len(G.nodes)/2), math.ceil(len(G.nodes)/2)]:
#     num_cut_edges = 0
#     for u, v in G.edges:
#         num_cut_edges += sample[u] + sample[v] - 2*sample[u]*sample[v]
#     print("Valid partition found with", num_cut_edges, "cut edges.")
# else:
#     print("Invalid partition.")



# k = g.subgraph(result1_unique)

# import networkx as nx
# import itertools

# G = g
# all_connected_subgraphs = []

# # here we ask for all connected subgraphs that have at least 2 nodes AND have less nodes than the input graph
# for nb_nodes in range(2, G.number_of_nodes()):
#     for SG in (G.subgraph(selected_nodes) for selected_nodes in itertools.combinations(G, nb_nodes)):
#         if nx.is_connected(SG):
#             print(SG.nodes)
#             all_connected_subgraphs.append(SG)

# # subgraphs_of_G_ex, removed_edges = graph_partitioning(G=g, plotting=False)
# # print(removed_edges)
# print(all_connected_subgraphs)

# connected_component_subgraphs



# noadna
# with open('outfile.txt', 'w') as file:
#     file.writelines(subgraphs_of_G_ex)
# test = SCCManager(graphPoint)
# clusters = test.get_scc()


# result1_unique = [*set(result1)]
# # print(result1)

# mapper = {}

# for indexx in range(len(result1_unique)):
#     for i in range(len(clusters)):
#         for j in range(len(clusters[i])):
#             if clusters[i][j] == result1_unique[indexx]:
#                 mapper[clusters[i][j]] = i

# newweightGraph= []
# for ele in resWeighted:
#     # print(ele[0])
#     newweightGraph.append( 
#         [ele[0], ele[1], ele[2], mapper[ele[0]]]
#         )

# with open('outfile.txt', 'w') as file:
#     file.writelines('\t'.join(str(j) for j in i) + '\n' for i in newweightGraph)
# now = time.time()
# print("It has been {0} seconds since the loop started".format(now - start))