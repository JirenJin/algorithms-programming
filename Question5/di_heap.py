import heapq
import sys
filename = 'dijkstraData.txt'
lines = [line.strip('\r\n').split('\t')[:-1] for line in open(filename,
'r').readlines()]

for line in lines:
    line[:] = [map(int, el.split(',')) for el in line][1:]

def dijkstra(graph, s):
    global X
    global A
    X = []
    A = [1000000] * len(graph)
    V = range(1, len(graph) + 1)
    A[s - 1] = 0
    X.append(s) 
    while len(X) != len(graph):
        W = list(set(V).difference(set(X)))
        min_distance = float('inf')
        vertex_to_add = None
        for v in X:
            for edge in graph[v - 1]:
                if edge[0] in W:
                    if edge[1] + A[v - 1] < min_distance:
                        min_distance = edge[1] + A[v - 1]
                        vertex_to_add = edge[0]
        X.append(vertex_to_add)
        A[vertex_to_add - 1] = min_distance

def di_heap(graph, s):
    global X
    global A
    X = []
    A = [1000000] * len(graph)
    V = range(1, len(graph) + 1)
    A[s - 1] = 0
    X.append(s) 
    W = list(set(V).difference(set(X)))
    W = [(1000000, x) for x in W]
    heapq.heapify(W)
    print W
    w = s
    while len(X) != len(graph):
        for edge in graph[w - 1]:
            if edge[0] in 


dijkstra(lines, 1)
for i in (7, 37, 59, 82, 99, 115, 133, 165, 188, 197):
    sys.stdout.write(str(A[i - 1]) + ',') 

di_heap(lines, 1)
