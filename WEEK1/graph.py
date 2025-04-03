class Graph:
    def __init__(self,length):
        self.Vertices = []
        for i in range(1,length +1):
            self.Vertices.append(i)
        self.Edges = []
    def insert_edge(self,edge_start,edge_end,weight):
        if edge_start not in self.Vertices:
            print("Illegal Edge start point")
            return
        if edge_end not in self.Vertices:
            print("Illegal Edge end point")
            return
        self.Edges.append((edge_start,edge_end,weight))
    def print_AdjList(self):
        AdjList = {}
        for vertex in self.Vertices:
            AdjList[vertex] = []
        for edge in self.Edges:
            AdjList[edge[0]].append([edge[1],edge[2]])
        print(AdjList)
    def print_AdjMat(self):
        AdjMat = []
        for i in (self.Vertices):
            AdjMat.append([0]*len(self.Vertices))
        for edge in self.Edges:
            AdjMat[edge[0]-1][edge[1]-1] = edge[2]
        print(AdjMat)



gr = Graph(4)
gr.insert_edge(1,2,1)
gr.insert_edge(1,3,1)
gr.insert_edge(3,4,4)
gr.insert_edge(2,3,3)
gr.insert_edge(4, 1, 5)

gr.print_AdjList()
gr.print_AdjMat()

# output: {0: [[2, 1], [1, 1]], 1: [[2, 3]], 2: [[3, 4]], 3: []}
#[[0, 1, 1, 0], [0, 0, 3, 0], [0, 0, 0, 4], [0, 0, 0, 0]]
