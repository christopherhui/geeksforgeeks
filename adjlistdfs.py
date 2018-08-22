# Undirected graph DFS using dictionaries to implement val (strings, num, etc.)
class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = [u]
        else:
            self.graph[v].append(u)

    def DFS(self, s):
        visited = [False] * len(self.graph)
        visited[s] = True
        print(s)
        self.DFSUtil(s, visited)


    def DFSUtil(self, v, visited):
        for i in self.graph[v]:
            if visited[i] == False:
                visited[i] = True
                print(i)
                self.DFSUtil(i, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.DFS(2)
