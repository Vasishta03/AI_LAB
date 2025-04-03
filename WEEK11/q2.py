from queue import Queue

def checkInvalid(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j] or abs(arr[i] - arr[j]) == j-i:
                return True
    return False

queens_Size = 8
solns = []
queue = Queue()
queue.put([])
while not queue.empty():
    soln = queue.get()
    if checkInvalid(soln):
        continue
    if len(soln) == queens_Size:
        print(soln)
    for i in range(queens_Size):
        sol_copy = soln.copy()
        sol_copy.append(i)
        queue.put(sol_copy)

#(0, 4, 7, 5, 2, 6, 1, 3)
#(0, 5, 7, 2, 6, 3, 1, 4)
#(0, 6, 3, 5, 7, 1, 4, 2)
#…
#…
#(7, 3, 0, 2, 5, 1, 6, 4)