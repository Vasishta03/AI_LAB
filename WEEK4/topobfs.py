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

def BFS(graph):
    Visited = []
    Queue = []
    AdjList = graph.AdjList()
    for newvertex in graph.Vertices:
        Queue.append(newvertex)
        while len(Queue) != 0:
            vertex = Queue.pop(0)
            if vertex not in Visited:
                for neighbour in AdjList[vertex]:
                    Queue.append(neighbour[0])
            Visited.append(vertex)
    return Visited

def TopoLogOrder(uwdg):
        graph = uwdg.graph
        Visited = BFS(graph)
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
print("Is DAG:", uwdg.graph.is_dag())

"""No of Nodes:5
Enter start,end,-1,-1 to exit
0,1
0,2
1,0
1,2
2,1
-1,-1
3 4 0 1 2 """