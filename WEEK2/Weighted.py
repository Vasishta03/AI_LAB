from typing import List, Dict, Tuple
import numpy as np

class Graph:
    def __init__(self, length: int):
        self.vertices: List[int] = list(range(length))
        self.edges: List[Tuple[int, int, int]] = []

    def insert_edge(self, edge_start: int, edge_end: int, weight: int): 
        if edge_start not in self.vertices:
            raise ValueError(f"Invalid edge start point: {edge_start}")
        if edge_end not in self.vertices:
            raise ValueError(f"Invalid edge end point: {edge_end}")
        self.edges.append((edge_start, edge_end, weight))

    def get_adjlist(self) -> Dict[int, List[List[int]]]:
        adjlist = {vertex: [] for vertex in self.vertices}
        for edge in self.edges:
            adjlist[edge[0]].append([edge[1], edge[2]])
        return adjlist

    def get_adjmat(self) -> np.ndarray:
        adjmat = np.zeros((len(self.vertices), len(self.vertices)), dtype=int)
        for edge in self.edges:
            adjmat[edge[0]][edge[1]] = edge[2]
        return adjmat

class Weighted:
    def __init__(self):
        num_nodes = int(input("Enter Number of Nodes: "))
        self.graph = Graph(num_nodes)

    def menu(self):
        print("Enter <edge_start>,<edge_end>,<weight>  Enter -1,-1,-1 to exit")
        while True:
            try:
                a, b, c = map(int, input().split(","))
                if a == -1 or b == -1 or c == -1:
                    break
                self.graph.insert_edge(a, b, c)
            except ValueError as e:
                print(f"Error: {e}")
                continue

def main():
    wdg = Weighted()
    wdg.menu()
    print("\nAdjacency List:")
    adjlist = wdg.graph.get_adjlist()
    for vertex, edges in adjlist.items():
        print(f"{vertex}: {edges}")
    print("\nAdjacency Matrix:")
    adjmat = wdg.graph.get_adjmat()
    print(adjmat)
if __name__ == "__main__":
    main()


