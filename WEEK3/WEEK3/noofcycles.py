class Graph:
    def __init__(self,length):
        self.Vertices = []
        for i in range(length):
            self.Vertices.append(i)
        self.Edges = []
    def insert(self,ed_st,ed_end,weight):
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
    def is_dag(self):
        def dfs_cycle_check(vertex, visited, rec_stack):
            visited.add(vertex)
            rec_stack.add(vertex)
            adj_list = self.AdjList()
            for neighbor in adj_list.get(vertex, []):
                neighbor_vertex = neighbor[0]                
                if neighbor_vertex not in visited:
                    if dfs_cycle_check(neighbor_vertex, visited, rec_stack):
                        return True                
                elif neighbor_vertex in rec_stack:
                    return True      
            rec_stack.remove(vertex)
            return False      
        visited = set()
        rec_stack = set()        
        for vertex in self.Vertices:
            if vertex not in visited:
                if dfs_cycle_check(vertex, visited, rec_stack):
                    return False 
        return True 
    def TopologOr(self):
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
        print("Enter start,end -1,-1 to exit")
        while True:
            a,b = list(map(int,input().split(",")))
            if a == -1 or b == -1:
                return
            self.graph.insert(a,b,1)
def DFS(graph,startindex=0):
    Stack = []
    AdjList = graph.AdjList()
    Visited = []
    Stack.append(graph.Vertices[startindex])
    while len(Stack) != 0:
        vertex = Stack.pop()
        if vertex not in Visited:
            for neighbour in AdjList[vertex]:
                Stack.append(neighbour[0])
        Visited.append(vertex)
    return Visited
def NoOFCycles(gr,start):
    Visited = DFS(gr,start)
    print(Visited)
    sum = 0
    for vertex in set(Visited):
        sum += Visited.count(vertex)-1
    return sum
uwdg = UnWeighted()
uwdg.Menu()
print(NoOFCycles(uwdg.graph,2))
print("Is DAG:", uwdg.graph.is_dag())

