class CC:
    def __init__(self, graph):
        self.marked = [False] * graph.V
        self.id = [-1] * graph.V
        self.count = 0

        for v in range(graph.V):
            if not self.marked[v]:
                self.dfs(graph, v)
                self.count += 1

    def dfs(self, graph, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in graph.adj(v):
            if not self.marked[w]:
                self.dfs(graph, w)