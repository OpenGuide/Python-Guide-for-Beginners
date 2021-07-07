from collections import defaultdict
class graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.status = False
    def addgraph(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s, t):

        visited = [False] * (len(self.graph))

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            if s == t:
                print("found")
                self.status = True
                break

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        if self.status == False:
            print("Not Found")


g = graph()
g.addgraph(0, 1)
g.addgraph(0, 2)
g.addgraph(1, 2)
g.addgraph(2, 0)
g.addgraph(2, 3)
g.addgraph(3, 3)

print ("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(int(input("starting node : ")),int(input("Target : ")))
