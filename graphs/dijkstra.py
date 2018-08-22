class Graph:
    def __init__(self, V):
        self.vertices = V
        self.graph = {}
        for i in range(1, self.vertices + 1):
            self.graph[i] = list()

    def add_edges(self):
        for i in range(1, self.vertices + 1):
            if i + 1 in self.graph:
                self.graph[i].append(i + 1)
            if 3 * i in self.graph:
                self.graph[i].append(3 * i)

    def shortest_path(self, s):
        if s == self.vertices:
            return 0
        else:
            max = 0
            for i in self.graph[s]:
                if i > max:
                    max = i
            return 1 + self.shortest_path(max)

t = int(input())
for i in range(t):
    n = int(input())
    graph = Graph(n)
    graph.add_edges()
    print(graph.shortest_path(1))

