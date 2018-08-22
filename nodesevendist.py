class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
        self.graph[v] = list()

    def DFS(self, s):
        visited = {}
        for i in self.graph:
            visited[i] = False
        visited[s] = True
        self.DFSUtil(s, visited)

    def DFSUtil(self, v, visited):
        count = 0
        for i in self.graph[v]:
            if visited[i] == False:
                visited[i] = True
                if (i - v) % 2 == 0:
                    count += (i - v) / 2
                print(count)
                self.DFSUtil(i, visited)


t = int(input())
for _ in range(t):
    n = int(input())
    aList = [int(x) for x in input().split()]
    graph = Graph()
    for i in range(0, len(aList), 2):
        x = aList[i]
        y = aList[i + 1]
        graph.add_node(x, y)
    graph.DFS(min(graph.graph))