import copy
import random

f = open("kargerMinCut.txt", 'r')
# get each row of the gragh ajaciency list
graph = [line.strip("\r\n") for line in f.readlines()]

# get a dictionaly whose keys are each vertice of the graph
# value are edges.
graph_dict = {}
for i in xrange(len(graph)):
    graph_dict[str(i+1)] = graph[i].split('\t')[1:-1]
print graph_dict

# function to find the minimus_cut once
def find_min_cut(graph_dict):

    # if the number of vertices is greater than 2, then comtract the graph
    while len(graph_dict) > 2:
        # choose the random vertice of the edge will be contracted
        first_vertice = random.choice(graph_dict.keys()) 
        # get and delete the vertice list in graph_dict
        first_vertice_list = graph_dict.pop(first_vertice)
        # choose the other vertice of the edge
        second_vertice = random.choice(first_vertice_list)
        #print vertice, 'vertice'
        #print graph_dict[vertice].count(str(first_vertice))

        # remove the edge in second_vertice list
        for i in xrange(graph_dict[second_vertice].count(first_vertice)):
            graph_dict[second_vertice].remove(first_vertice)
        # modify other edges' vertices from first_vertice to second_vertice
        for other in first_vertice_list:
            if other != second_vertice:
                for i in xrange(graph_dict[other].count(first_vertice)):
                    index = graph_dict[other].index(first_vertice)
                    graph_dict[other][index] = second_vertice
                # append other edges to second_vertice
                graph_dict[second_vertice].append(other)

        #print graph_dict 
    #print len(graph_dict[vertice]), 'mincut'

    # return the remained edges
    return len(graph_dict[second_vertice])

x = float('inf')
# rerun the function N times, to find the minimum cut
for i in range(1000):
    # in each loop, we have to ensure that the graph is not changed
    graph_test = copy.deepcopy(graph_dict)
    result = find_min_cut(graph_test)
    if x > result:
        x = result
print x

"""first_vertice = random.choice(graph_dict.keys()) 
print first_vertice, 'first_vertice'
first_vertice_list = graph_dict.pop(first_vertice)    
print first_vertice_list, 'first_vertice_list'
vertice = random.choice(first_vertice_list)
print vertice, 'vertice'
print graph_dict[vertice].count(str(first_vertice)) 
for i in xrange(graph_dict[vertice].count(first_vertice)):
    graph_dict[vertice].remove(first_vertice)
for other in first_vertice_list:
    if other != vertice:
        for i in xrange(graph_dict[other].count(first_vertice)):
            index = graph_dict[other].index(first_vertice)
            graph_dict[other][index] = vertice
print graph_dict
"""

