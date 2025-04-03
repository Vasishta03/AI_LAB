from collections import deque

def bfs(cap_a, cap_b, target):
    queue = deque()
    visited = set()   
    init_state = (0, 0)
    queue.append((init_state, [])) 
    visited.add(init_state)
    while queue:
        (cur_a, cur_b), path = queue.popleft()        
        if cur_a == target or cur_b == target:
            return path + [(cur_a, cur_b)]        
        possible = [
            (cap_a, cur_b),  
            (cur_a, cap_b), 
            (0, cur_b),           
            (cur_a, 0),           
            (max(0, cur_a - (cap_b - cur_b)), min(cap_b, cur_b + cur_a)),  
            (min(cap_a, cur_a + cur_b), max(0, cur_b - (cap_a - cur_a)))   
        ]        
        for state in possible:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(cur_a, cur_b)]))    
    return None  

def dfs(cap_a, cap_b, target):
    stack = []
    visited = set()    
    init_state = (0, 0)
    stack.append((init_state, []))  
    visited.add(init_state)
    while stack:
        (cur_a, cur_b), path = stack.pop() 
        if cur_a == target or cur_b == target:
            return path + [(cur_a, cur_b)]        
        possible = [
            (cap_a, cur_b),  
            (cur_a, cap_b), 
            (0, cur_b),            
            (cur_a, 0),            
            (max(0, cur_a - (cap_b - cur_b)), min(cap_b, cur_b + cur_a)),  
            (min(cap_a, cur_a + cur_b), max(0, cur_b - (cap_a - cur_a)))   
        ]       
        for state in possible:
            if state not in visited:
                visited.add(state)
                stack.append((state, path + [(cur_a, cur_b)]))    
    return None  

if __name__ == "__main__":
    cap_a = 4  
    cap_b = 3  
    target = 2      
    print("Using BFS:")
    result_bfs = bfs(cap_a, cap_b, target)
    if result_bfs:
        for step in result_bfs:
            print(step)
    else:
        print("No soln.")
    print("\nUsing DFS:")
    result_dfs = dfs(cap_a, cap_b, target)
    if result_dfs:
        for step in result_dfs:
            print(step)
    else:
        print("No soln.")

#Using BFS:
#(0, 0)
#(0, 3)
#(3, 0)
#(3, 3)
#(4, 2)

#Using DFS:
#(0, 0)
#(0, 3)
#(3, 0)
#(3, 3)
#(4, 2)
