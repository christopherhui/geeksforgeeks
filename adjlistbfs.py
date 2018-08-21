# Graph class for integer values starting from 0 to V
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

    def BFS(self, s):
        visited = [False] * self.vertices
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.BFS(2)


