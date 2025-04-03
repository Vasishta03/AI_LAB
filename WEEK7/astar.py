class Graph:
    def __init__(self,length):
        self.Vertices = []
        for i in range(length):
            self.Vertices.append(i)
        self.Edges = []
    def insert(self,edge_st,edge_end,weight):
        if edge_st not in self.Vertices:
            print("Illegal st pt")
            return
        if edge_end not in self.Vertices:
            print("Illegal end pt")
            return
        self.Edges.append((edge_st,edge_end,weight))
    def AdjList(self):
        AdjList = {}
        for vertex in self.Vertices:
            AdjList[vertex] = []
        for edge in self.Edges:
            AdjList[edge[0]].append([edge[1],edge[2]])
        return AdjList
    def print_AdjMat(self):
        AdMat = []
        for i in range(len(self.Vertices)):
            AdjMat.append([0]*len(self.Vertices))
        for edge in self.Edges:
            AdjMat[edge[0]][edge[1]] = edge[2]
        print(AdjMat)

def AStar(graph,start,goals,Heuristic):
    Visited,Queue,AdjList = [],[],graph.AdjList()
    Queue.append([[start],Heuristic[start],0])
    while len(Queue) != 0:
        vertex_min,i_min = Queue[0],0
        for i,vert in enumerate(Queue):
            if vert[1] <= vertex_min[1]:
                vertex_min = vert
                i_min = i
        Queue.pop(i_min)
        if vertex_min[0][-1] in goals:
            Visited.append(vertex_min[0][-1])
            return vertex_min[0],vertex_min[2]
        if vertex_min[0] not in Visited:
            for neigh in AdjList[vertex_min[0][-1]]:
                pah = vertex_min[0].copy()
                pah.append(neigh[0])
                Queue.append([pah,Heuristic[neigh[0]]+vertex_min[2]+neigh[1],neigh[1]+vertex_min[2]])


Nodes = input("Nodes:").split(",")
Heuristic = list(map(int,input("Heuristic Val: ").split(",")))
mapping = {}
for i in range(len(Nodes)):
    mapping[Nodes[i]] = i
graph = Graph(len(Nodes))
print("Enter st,end,weight (-1,-1,-1 to exit):")
while True:
    a,b,c = input().split(",")
    if a == "-1" or b == "-1" or c == "-1":
        break
    graph.insert(mapping[a],mapping[b],int(c))
start = mapping[input("Start:")]
goals = input("Goals:").split(",")
for i in range(len(goals)):
    goals[i] = mapping[goals[i]]
print(graph.AdjList())
path,cost = AStar(graph,start,goals,Heuristic)
for i in range(len(path)):
    path[i] = Nodes[path[i]]

print("Optimal path: ",path)
print("Cost of path: "+str(cost))


"""
Nodes:A,B,C,D,E,F,G,H,I,J
Heuristic Val: 10,8,5,7,3,6,5,3,1,0
Enter st,end,weight (-1,-1,-1 to exit):
A,B,6
A,F,3
B,D,2
B,C,3
C,D,1
C,E,5
E,D,8
E,I,5
E,J,5
I,J,3
G,I,3
I,H,2
F,H,7
F,G,1
-1,-1,-1
Start:A
Goals:J
{0: [[1, 6], [5, 3]], 1: [[3, 2], [2, 3]], 2: [[3, 1], [4, 5]], 3: [], 4: [[3, 8], [8, 5], [9, 5]], 5: [[7, 7], [6, 1]], 6: [[8, 3]], 7: [], 8: [[9, 3], [7, 2]], 9: []}
Optimal path:  ['A', 'F', 'G', 'I', 'J']
Cost of path: 10
"""