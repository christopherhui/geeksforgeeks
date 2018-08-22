class Graph:

    def __init__(self, V):
        self.vertices = V
        self.graph = {}
        for i in range(self.vertices):
            self.graph[i] = list()

    def add_edge(self, u, v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def DFS(self, s):
        visited = [False] * self.vertices
        visited[s] = True
        print(s)
        self.DFSUtil(s, visited)


    def DFSUtil(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                visited[i] = True
                print(i)
                self.DFSUtil(i, visited)

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.DFS(2)
