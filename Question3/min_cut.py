import copy
import random
f = open("kargerMinCut.txt", 'r')
graph = [line.strip("\r\n") for line in f.readlines()]
print graph
graph_dict = {}
for i in xrange(len(graph)):
    graph_dict[str(i+1)] = graph[i].split('\t')[1:-1]
print graph_dict
#for i in xrange(10):
#    print random.randint(1,4)
def find_min_cut(graph_dict):
    while len(graph_dict) > 2:
        contraction = random.choice(graph_dict.keys()) 
        #print contraction
        contraction_row = graph_dict.pop(contraction)
        #print contraction_row, 'contraction_row'
        vertice = random.choice(contraction_row)
        #print vertice, 'vertice'
        #print graph_dict[vertice].count(str(contraction))
        for i in xrange(graph_dict[vertice].count(contraction)):
            graph_dict[vertice].remove(contraction)
        for other in contraction_row:
            if other != vertice:
                for i in xrange(graph_dict[other].count(contraction)):
                    index = graph_dict[other].index(contraction)
                    graph_dict[other][index] = vertice
                graph_dict[vertice].append(other)
        #print graph_dict 
    #print len(graph_dict[vertice]), 'mincut'
    return len(graph_dict[vertice])

graph_test = copy.deepcopy(graph_dict)
find_min_cut(graph_test)
x = float('inf')
for i in range(1000):
    graph_test = copy.deepcopy(graph_dict)
    result = find_min_cut(graph_test)
    if x > result:
        x = result
print x

"""contraction = random.choice(graph_dict.keys()) 
print contraction, 'contraction'
contraction_row = graph_dict.pop(contraction)    
print contraction_row, 'contraction_row'
vertice = random.choice(contraction_row)
print vertice, 'vertice'
print graph_dict[vertice].count(str(contraction)) 
for i in xrange(graph_dict[vertice].count(contraction)):
    graph_dict[vertice].remove(contraction)
for other in contraction_row:
    if other != vertice:
        for i in xrange(graph_dict[other].count(contraction)):
            index = graph_dict[other].index(contraction)
            graph_dict[other][index] = vertice
print graph_dict
"""

