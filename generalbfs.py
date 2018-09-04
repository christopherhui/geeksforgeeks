from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.vertices = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, s):
        visited = [False] * self.vertices
        queue = [s]
        seqList = [s]
        visited[s-1] = True

        while queue:
            s = queue.pop(0)

            for v in self.graph[s]:
                if visited[v-1] == False:
                    visited[v-1] = True
                    queue.append(v)
                    seqList.append(v)

        return seqList

t = int(input())
g = Graph(t)
for i in range(t-1):
    aList = [int(x) for x in input().split()]
    g.add_edge(aList[0], aList[1])
match = [int(x) for x in input().split()]
if match == g.bfs(1):
    print("Yes")
else:
    print("No")




