from graph import Graph
from cc import CC
from bfs_paths import BFSPaths
from cycle import Cycle

def build_graph():
    g = Graph(9)

    edges = [
        (0,7),(0,5),
        (1,8),(1,6),
        (2,7),(2,3),
        (3,8),
        (5,6)
    ]

    for v, w in edges:
        g.add_edge(v, w)

    return g

def main():
    g = build_graph()

    print("Lista de adjacência:")
    print(g)

    cc = CC(g)
    print("Componentes conexas:", cc.count)

    componentes = {}
    for v in range(g.V):
        componentes.setdefault(cc.id[v], []).append(v)

    for k in componentes:
        print(f"Componente {k}:", componentes[k])

    bfs = BFSPaths(g, 0)
    print("Distância mínima (0 -> 8):", bfs.distance_to(8))

    cycle = Cycle(g)
    print("Possui ciclo:", "Sim" if cycle.has_cycle else "Não")

if __name__ == "__main__":
    main()