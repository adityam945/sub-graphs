import random

def randNum(min_val, max_val):
    return random.randint(min_val, max_val)


def runForRndGen(total_nodes, total_destn, total_sub_graphs, index):
    total_nodes = total_nodes
    total_destn = total_destn
    total_sub_graphs = total_sub_graphs

    src = [] 
    dest = []
    weigth = []
    label = []

    for i in range(1, total_nodes):
        # points
        edges = randNum(1, total_destn)    
        dest_counter = []

        for j in range(edges):
            src.append(i)
            dest_ = randNum(1, total_nodes) 
            while dest_ == i or dest_ in dest_counter:
                dest_ = randNum(1, total_nodes) 
            dest.append(dest_)
            dest_counter.append(dest_)
            label.append(randNum(1, total_sub_graphs))
            weigth.append(randNum(1, 100))

        # print(src, dest, label, weigth)
            
    import pandas as pd

    df = pd.DataFrame()
    df['src'] = src
    df['dest'] = dest
    df['weight'] = weigth
    df['Label'] = label
    # print(df.head())
    import numpy as np
    # print(df.shape, 'edges')

    df.to_csv('output' + '_' + str(df.shape) + '_' + str(index) + '_' + str(total_nodes) + '_' + str(total_destn) + '_' + str(total_sub_graphs) +'.txt', index=False, header=False, sep=' ')



def main():
    for i in range(5):

        runForRndGen(10000, 120, 10, i)
        print('Gen', i)


main()
# for i in range(len(total_nodes)):
#     total_nodes_list.append(i)


# for i in range(len(total_sub_graphs)):




# for i in range(total_nodes):
#     if i % 100 == 0:
#         print('In', i)
#     subgraph = random.randint(0,total_sub_graphs)
    
#     randomlist_dests = random.sample(range(0, total_nodes - 1), total_destn)
#     # randomlist_subgraph = random.sample(range(1, 100), 500)


#     for j in range(len(randomlist_dests)):
#         graph_line = []
#         graph_line.append(i)
#         graph_line.append(randomlist_dests[j])
#         weigth = random.randint(0,100)
#         graph_line.append(weigth)
#         # random subgraph

#         graph_line.append(subgraph)
#         graph.append(graph_line)



# # print(graph)
# with open('outfile1.txt', 'w') as file:
#     file.writelines('\t'.join(str(j) for j in i) + '\n' for i in graph)