class scc:
    is_explored = [] 
    finished_times = {} 
    start_node = 0
    search_stack = []
    leader = {} 
    index = 1 

    def initial(self, total_nodes):
        self.is_explored = [False] * total_nodes
        self.start_node = None

    def DFS(self, graph, node_i, reverse):
        number = node_i
        self.search_stack.append(node_i)
        while(True):
            self.is_explored[number - 1] = True
            if reverse == False:
                self.leader[self.start_node].append(number - 1)
                #self.leader[number - 1] = self.start_node
            for node_j in graph[number - 1]:
                if len(graph[number -1]) == 0:
                    break
                if self.is_explored[node_j - 1] == False:
                    self.search_stack.append(node_j)
                    number = node_j
                    break
            else:
                if len(self.search_stack) == 0:
                    break
                else:
                    self.finished_times[self.index] = self.search_stack.pop()
                    self.index += 1
                    if len(self.search_stack) != 0:
                        number = self.search_stack[-1]
                    
    def DFS_loop(self, graph, reverse):
        if reverse == True:
            for i in range(len(graph), 0, -1):
                if self.is_explored[i - 1] == False:
                    self.start_node = i
                    self.leader[self.start_node] = []
                    self.DFS(graph, i, reverse)

        else:
            for i in range(len(graph), 0, -1):
                if self.is_explored[self.finished_times[i] - 1] == False:
                    self.start_node = self.finished_times[i] 
                    self.leader[self.start_node] = []
                    self.DFS(graph, self.start_node, reverse)

lines = open('SCC.txt', 'r').readlines()
edges = [line.strip('\r\n').split(' ') for line in lines]
graph = [[] for row in range(875714)]
graph_reverse = [[] for row in range(875714)]
for edge in edges:
    graph[int(int(edge[0]) - 1)].append(int(edge[1]))
    graph_reverse[int(int(edge[1]) - 1)].append(int(edge[0]))

a = scc()
a.initial(875714)
a.DFS_loop(graph, 1)
a.leader = {}
a.initial(875714)
a.DFS_loop(graph, 0)

size = []
for key in a.leader.keys():
    print len(a.leader[key])
    size.append(len(a.leader[key]))
print size
size = sorted(size)
print size[-5:]
