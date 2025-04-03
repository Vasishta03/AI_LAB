#8queens using hill climb search algorithm

def Queens_Score(queens):
    score = 0
    for p in range(len(queens)):
        for q in range(p+1,len(queens)):
            if queens[p] != queens[q] and abs(queens[p] - queens[q]) != q-p:
                score += 1
    return score

Cur_State = [4,1,8,4,1,7,3,6]

while True:
    neighb = []
    for i in range(len(Cur_State)):
        if Cur_State[i] < 8:
            nxt_state = Cur_State.copy()
            nxt_state[i] += 1
            neighb.append([Queens_Score(nxt_state),nxt_state])
        if Cur_State[i] > 1:
            nxt_state = Cur_State.copy()
            nxt_state[i] -= 1
            neighb.append([Queens_Score(nxt_state),nxt_state])
    neighb = sorted(neighb, key=lambda x:x[0])
    if neighb[-1][0] >= 28:
        print("Soln is ",neighb[-1][1])
        break
    Cur_State = neighb[-1][1]
    
print(Queens_Score([5,1,8,4,2,7,3,6]))

#Soln is  [5, 1, 8, 4, 2, 7, 3, 6]
#28
