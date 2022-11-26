
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
# print(resWeighted)

test = SCCManager(graphPoint)
clusters = test.get_scc()
for i in clusters:
    print(i)

now = time.time()
print("It has been {0} seconds since the loop started".format(now - start))