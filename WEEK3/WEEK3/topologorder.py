class Graph:
    def __init__(self,length):
        self.Vertices = []
        for i in range(length):
            self.Vertices.append(i)
        self.Edges = []
    def insert_edge(self,ed_st,ed_end,weight):
        if ed_st not in self.Vertices:
            print("Illegal start pt")
            return
        if ed_end not in self.Vertices:
            print("Illegal end pt")
            return
        self.Edges.append((ed_st,ed_end,weight))
    def AdjList(self):
        AdjList = {}
        for vertex in self.Vertices:
            AdjList[vertex] = []
        for edge in self.Edges:
            AdjList[edge[0]].append([edge[1],edge[2]])
        return AdjList
    def AdjMat(self):
        AdjMat = []
        for i in range(len(self.Vertices)):
            AdjMat.append([0]*len(self.Vertices))
        for edge in self.Edges:
            AdjMat[edge[0]][edge[1]] = edge[2]
        return AdjMat
    def TopoLogOrder(self):
        InDeg = [0]*len(self.Vertices)
        AdjMat = self.AdjMat()
        for i in range(len(self.Vertices)):
            sum = 0
            for j in range(len(self.Vertices)):
                sum += AdjMat[j][i]
            InDeg[i] = sum
        Topo = sorted(enumerate(InDeg), key=lambda i: i[1])
        for elem in Topo:
            print(elem[0],end=' ')
        print()                                                                                                                    
class UnWeighted:
    def __init__(self):
        self.graph = Graph(int(input("No of Nodes:")))
    def Menu(self):
        print("Enter start,end,-1,-1 to exit")
        while True:
            a,b = list(map(int,input().split(",")))
            if a == -1 or b == -1:
                return
            self.graph.insert_edge(a,b,1)
def DFS(graph):
    Visited = []
    Stack = []
    AdjList = graph.AdjList()
    for newvertex in graph.Vertices:
        Stack.append(newvertex)
        while len(Stack) != 0:
            vertex = Stack.pop()
            if vertex not in Visited:
                for neighbour in AdjList[vertex]:
                    Stack.append(neighbour[0])
            Visited.append(vertex)
    return Visited
def TopoLogOrder(uwdg):
        graph = uwdg.graph
        Visited = DFS(graph)
        Topo = []
        for vertex in graph.Vertices:
            Topo.append(Visited.count(vertex)-1)
        Topo = sorted(enumerate(Topo), key=lambda i: i[1])
        for elem in Topo:
            print(elem[0],end=' ')
        print()
uwdg = UnWeighted()
uwdg.Menu()
TopoLogOrder(uwdg)