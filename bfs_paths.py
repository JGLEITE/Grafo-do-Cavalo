from collections import deque

class BFSPaths:
    def __init__(self, graph, source):
        self.source = source
        self.marked = [False] * graph.V
        self.edge_to = [-1] * graph.V
        self.dist_to = [-1] * graph.V
        self.bfs(graph, source)

    def bfs(self, graph, s):
        queue = deque([s])
        self.marked[s] = True
        self.dist_to[s] = 0

        while queue:
            v = queue.popleft()
            for w in graph.adj(v):
                if not self.marked[w]:
                    self.marked[w] = True
                    self.edge_to[w] = v
                    self.dist_to[w] = self.dist_to[v] + 1
                    queue.append(w)

    def distance_to(self, v):
        return self.dist_to[v]