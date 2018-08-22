from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        if u > self.vertices or v > self.vertices:
            raise ValueError("Value of u or v is greater than number of vertices.")
        self.graph[u].append(v)

a = Graph(5)
a.addEdge(0, 1)
a.addEdge(2, 3)
a.addEdge(0, 2)
a.addEdge(1, 2)
a.addEdge(3, 4)
a.addEdge(4, 2)
a.addEdge(4, 1)

