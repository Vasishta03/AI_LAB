Y = [(0,0),(0,0),(0,0),(0,0)]
X = [(0,4),(0,3),(0,2),(0,1)]
EDist = []

if len(X) != len(Y):
    sys.exit(0)

# Caluculate Euclidian Distances
for i in range(len(X)):
    EDist.append((abs(((X[i][0]-Y[i][0])**2) + ((X[i][1]-Y[i][1])**2)))**0.5)

# Bubble Sort
for j in range(len(EDist)-1):
    for i in range(len(EDist)-1-j):
        if EDist[i+1] < EDist[i]:
            EDist[i+1],EDist[i] = EDist[i],EDist[i+1]

print(EDist)

#[1.0, 2.0, 3.0, 4.0]
