import sys
sys.setrecursionlimit(300000)
class scc:
    is_explored = []
    leader = []
    t = 0
    s = None
    finish_time = []
    def initial(self,total_nodes):
        self.is_explored = [False] * total_nodes
        self.leader = [0] * total_nodes 
        self.finish_time = [0] * total_nodes
    def DFS(self, graph, node_i):
        self.is_explored[node_i - 1] = True 
        self.leader[node_i - 1] = self.s

        for node_j in graph[node_i - 1]:
            if self.is_explored[node_j - 1] == False:
                self.DFS(graph, node_j)

        self.t += 1
        self.finish_time[node_i -1] = self.t

    def DFS_loop(self, graph):
        self.t = 0
        self.s = None
        print len(graph), 'length of graph'
        for i in range(len(graph), 0, -1):
            if self.is_explored[i-1] == False:
                self.s = i
                self.DFS(graph, i)

lines = open('SCC.txt','r').readlines()
edges = [line.strip('\r\n').split(' ')[:-1] for line in lines]
edges = [[int(el[0]), int(el[1])] for el in edges]
print edges[:10]
edges_reverse = []
for edge in edges:
    edges_reverse.append([edge[1], edge[0]])
print edges_reverse[:10]

graph = [[] for row in range(875714)] 
graph_reverse = [[] for row in range(875714)] 
for edge in edges:
    graph[edge[0] - 1].append(edge[1])

for edge in edges_reverse:
    graph_reverse[edge[0] - 1].append(edge[1])

print graph[:5]
print graph_reverse[:5]

a = scc()
a.initial(875714)
a.DFS_loop(graph_reverse)
print a.finish_time[:10]
