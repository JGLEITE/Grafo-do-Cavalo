class Cycle:
    def __init__(self, graph):
        self.marked = [False] * graph.V
        self.has_cycle = False

        for v in range(graph.V):
            if not self.marked[v]:
                self.dfs(graph, v, -1)

    def dfs(self, graph, v, parent):
        self.marked[v] = True
        for w in graph.adj(v):
            if not self.marked[w]:
                self.dfs(graph, w, v)
            elif w != parent:
                self.has_cycle = True