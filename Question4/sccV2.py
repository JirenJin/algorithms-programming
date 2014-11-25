class scc:
    is_explored = []     # to record if the vertex has been explored
    finished_times = {}  # to record finished times of each vertex
    start_node = None    # define the leaders in 2nd pass (current source)
    search_stack = []    # search_stack for DFS recursion
    leaders = {}         # to store the vertex which has the same leader
                         # belong to the same SCC
    index = 1            # for finished times index
    t = 0                # for finishing times in 1st pass
                         # number of nodes processed so far

    def DFS(self, graph, node_i, reverse):
        '''Depth First Search, reverse is the flag of 
           if the graph is reversed and which loop it is
           ie. 1st loop or 2nd loop.'''

        number = node_i
        self.search_stack.append(number)
        self.is_explored[number - 1] = True
        if reverse == False:
            self.leaders[self.start_node].append(number)

        # if the length of stack isn't zero, then recursion
        while(len(self.search_stack) != 0):
            # if the vertex doesn't have outgoing edges
            # then it's the sink vertex
            if len(graph[number - 1]) == 0:
                # if reverse == true, then it's the 1st loop
                # we need to compute the finished times of each sink vertex
                if reverse == True:
                    self.t += 1
                    self.finished_times[self.t] = number
                self.search_stack.pop()
                if len(self.search_stack) != 0:
                    number = self.search_stack[-1]
                continue
            
            # recursive search each vertex
            for node_j in graph[number - 1]:
                if self.is_explored[node_j - 1] == False:
                    number = node_j
                    self.is_explored[number - 1] = True
                    # for every explored vertex, we store it
                    # with the same leader
                    if reverse == False:
                        self.leaders[self.start_node].append(number)
                    self.search_stack.append(number)
                    break
            # if we can't find a next vertex which hasn't been explored
            # then the vertex now, is the sink vertex
            else:
                if reverse == True:
                    self.t += 1
                    self.finished_times[self.t] = number
                self.search_stack.pop()
                if len(self.search_stack) != 0:
                    number = self.search_stack[-1]

                        

    def DFS_loop(self, graph, reverse):
        # initial the is_explored
        self.is_explored = [False] * len(graph)
        if reverse == True:
            self.t = 0
            for i in range(len(graph), 0, -1):
                if self.is_explored[i - 1] == False:
                    self.start_node = i
                    self.DFS(graph, i, reverse)

        else:
            for i in range(len(graph), 0, -1):
                # in the 2nd loop, we use finished_times as index
                if self.is_explored[self.finished_times[i] - 1] == False:
                    self.start_node = self.finished_times[i] 
                    self.leaders[self.start_node] = []
                    self.DFS(graph, self.start_node, reverse)
import time
start = time.time()
start2 = time.clock()

total_nodes = 875714 
lines = open('SCC.txt', 'r').readlines()
edges = [line.strip('\r\n').split(' ') for line in lines]
graph = [[] for row in range(total_nodes)]
graph_reverse = [[] for row in range(total_nodes)]
for edge in edges:
    graph[int(int(edge[0]) - 1)].append(int(edge[1]))
    graph_reverse[int(int(edge[1]) - 1)].append(int(edge[0]))

a = scc()
# the 1st pass
a.DFS_loop(graph_reverse, 1)
# the 2nd pass
a.DFS_loop(graph, 0)

size = []
# store each SCCs' size in size[]
for key in a.leaders.keys():
    size.append(len(a.leaders[key]))
# sort the sizes of SCCs
size.sort()
biggest_5 = size[:-6:-1]
print biggest_5 

end = time.time()
end2 = time.clock()
print end - start
print end2 - start2
#print a.finished_times
#print a.leaders
