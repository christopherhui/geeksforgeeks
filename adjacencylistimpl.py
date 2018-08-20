class Graph:
    def __init__(self, V):
        self.vertex = V
        self.vertices = {}

    for i in range(0, self.vertex):
        self.vertices[i] = list()

    def addEdges(self, V, E):
        if V in self.vertices and E in self.vertices:
            self.vertices[V].append(E).sort()
            self.vertices[E].append(V).sort()


t = int(input())
for _ in range(t):
    aList = [int(x) for x in input().split()]
    v = aList[0]
    e = aList[1]
    graph = Graph(v)

    for _ in range(e):
        bList = [int(x) for x in input().split()]
        graph.addEdges(bList[0], bList[1])


