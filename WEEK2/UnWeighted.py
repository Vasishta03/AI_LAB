class Graph:
    def __init__(self, length: int):
        self.vertices: List[int] = list(range(length))
        self.edges: List[Tuple[int, int, int]] = []

    def insert_edge(self, edge_start: int, edge_end: int, weight: int = 1):
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

    def get_adjmat(self) -> List[List[int]]:
        adjmat= [[0] * len(self.vertices) for _ in range(len(self.vertices))]
        for edge in self.edges:
            adjmat[edge[0]][edge[1]] = edge[2]
        return adjmat

class UnWeighted:
    def __init__(self):
        num_nodes = int(input("No of Nodes: "))
        self.graph = Graph(num_nodes)
    def menu(self):
        print("Enter <edge_start>,<edge_end>  Enter -1,-1 to exit")
        while True:
            try:
                a, b = map(int, input().split(",")) 
                if a == -1 or b == -1:
                    break   
                self.graph.insert_edge(a, b)
            except ValueError as e:
                print(f"Error: {e}")
                continue

def main():
    uwdg = UnWeighted()
    uwdg.menu()
    
    print("\nAdjacency List:")
    adjlist = uwdg.graph.get_adjlist()
    for vertex, edges in adjlist.items():
        print(f"{vertex}: {edges}")
    
    print("\nAdjacency Matrix:")
    adjmat = uwdg.graph.get_adjmat()
    for row in adjmat:
        print(row)

if __name__ == "__main__":
    main()


"""Enter Number of Nodes: 5
Enter <edge_start>,<edge_end>  Enter -1,-1 to exit
0,1
1,2
2,0
2,1
3,2
4,5
Error: Invalid edge end point: 5
5,4
Error: Invalid edge start point: 5
-1,-1

Adjacency List:
0: [[1, 1]]
1: [[2, 1]]
2: [[0, 1], [1, 1]]
3: [[2, 1]]
4: []

Adjacency Matrix:
[0, 1, 0, 0, 0]
[0, 0, 1, 0, 0]
[1, 1, 0, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 0, 0, 0]
"""