class Graph:
    def __init__(self, V):
        self.V = V
        self.adj_list = [[] for _ in range(V)]

    def add_edge(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def adj(self, v):
        return self.adj_list[v]

    def __str__(self):
        result = ""
        for v in range(self.V):
            result += f"{v}: " + " ".join(map(str, self.adj_list[v])) + "\n"
        return result