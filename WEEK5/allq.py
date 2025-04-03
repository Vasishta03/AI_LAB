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

def BFS(graph,start,goal=[0]):
    Visited = []
    Queue = []
    AdjList = graph.AdjList()
    Queue.append([[start],0])
    while len(Queue) != 0:
        vertex,min_val,i_min = Queue[0][0],Queue[0][1],0
        for i in range(len(Queue)):
            if Queue[i][1] < min_val:
                min_val = Queue[i][1]
                vertex = Queue[i][0]
                i_min = i
        Queue.pop(i_min)
        if vertex[-1] in goal:
            Visited.append(vertex[-1])
            return vertex,min_val
        if vertex[-1] not in Visited:
            for neighb in AdjList[vertex[-1]]:
                pah = vertex.copy()
                pah.append(neighb[0])
                Queue.append([pah,neighb[1]+min_val])
        Visited.append(vertex[-1])
    print("Goal Node Not Found!")

Nodes = input("Enter Nodes:").split(",")
mapping = {}
for i in range(len(Nodes)):
    mapping[Nodes[i]] = i
graph = Graph(len(Nodes))

print("Enter st, end, weight (-1,-1,-1 to exit)")
while True:
    a,b,c = input().split(",")
    if a == "-1" or b == "-1" or c == "-1":
        break
    graph.insert_edge(mapping[a],mapping[b],int(c))
start = mapping[input("Start:")]
goals = input("Goals:").split(",")

for i in range(len(goals)):
    goals[i] = mapping[goals[i]]
path,cost = BFS(graph,start,goals)

for i in range(len(path)):
    path[i] = Nodes[path[i]]

print("Optimal path(BFS) is ",path)
print("Cost: "+str(cost))


"""
q1 input

Enter Nodes:0,1,2,3,4,5,6,7,8,9
Enter st, end, weight (-1,-1,-1 to exit)
0,1,5
0,2,9
3,0,6
0,4,9
1,5,9
1,2,3
2,1,2
2,3,1
3,6,5
3,9,7
4,3,2
9,4,2
9,8,8
4,7,2
7,8,7
-1,-1,-1
Start:0
Goals:5,8
Optimal path(BFS) is  ['0', '1', '5']
Cost: 14

q2 input

Enter Nodes:S,1,2,3,4,5,G
Enter st, end, weight (-1,-1,-1 to exit)
S,1,2
S,3,5
3,1,5
3,G,6
3,4,2
1,G,1
G,4,7
2,1,4
4,2,4
4,5,3
5,2,6
5,G,3
-1,-1,-1
Start:S
Goals:G
Optimal path(BFS) is  ['S', '1', 'G']
Cost: 3

q3 input

Enter Nodes:Feering,Maldon,Clacton,Tiptree,Harwich,Blaxhall,Dunwich
Enter st, end, weight (-1,-1,-1 to exit)
Feering,Maldon,11
Clacton,Maldon,40
Maldon,Tiptree,8
Tiptree,Feering,3
Tiptree,Clacton,29
Harwich,Tiptree,31
Clacton,Harwich,17
Feering,Blaxhall,46
Harwich,Blaxhall,40
Blaxhall,Dunwich,15
Dunwich,Blaxhall,17
Harwich,Dunwich,53
-1,-1,-1
Start:Feering
Goals:Dunwich
Optimal path(BFS) is  ['Feering', 'Blaxhall', 'Dunwich']
Cost: 61

"""
