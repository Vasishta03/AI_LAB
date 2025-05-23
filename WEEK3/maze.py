StPt = 1
EndPt = 5

Maze = {1: [2, 6], 2: [1, 3], 3: [2, 8], 4: [5], 5: [4, 10], 6: [1, 11], 7: [8], 8: [3, 7], 9: [10, 14], 
        10: [5, 9, 15], 11: [6, 12], 12: [11, 17], 13: [14], 14: [9, 13, 19], 15: [10, 20], 
        16: [17], 17: [12, 16, 18], 18: [17, 19], 19: [14, 18], 20: [15]}

def Search(Maze, StPt, EndPt):
    Visited = []
    Stack = []
    Stack.append(StPt)
    while Stack:
        vertex = Stack.pop()
        if vertex not in Visited:
            Visited.append(vertex)
            if vertex == EndPt:
                print(Visited)
                return
            for conn in Maze[vertex]:
                Stack.append(conn)

Search(Maze, StPt, EndPt)
