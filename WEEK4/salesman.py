graph ={ 
'A': {'B': 2, 'C': 3, 'D': 1},
'B': {'A': 2, 'C': 4, 'D': 2},
'C': {'A': 3, 'B': 4, 'D': 3},
'D': {'A': 1, 'B': 2, 'C': 3}
}

man_st = "A"

Queue = []
Queue.append((man_st, 0))
while len(Queue) != 0:
	vertex, trav_dist = Queue.pop(0)
	if len(set(vertex)) >= len(graph) and vertex[-1] == man_st:
		print(vertex, trav_dist)
		break
	for neighbour in graph[vertex[-1]]:
		Queue.append((vertex+neighbour, trav_dist + graph[vertex[-1]][neighbour]))


#ABCDA 10