setplace=[[-2,1],[-2,-1],[2,-1],[-2,1],[-1,2],[-1,-2],[1,2],[1,-2]]
setTuple = [(1,2),(2,3),(1,2)]


for i in range(len(setTuple)):
    for j in range(len(setTuple)):
        if setplace[i][0] == setTuple[j][0] or setplace[i][1] == setTuple[j][1]:
            print(setTuple[i][0], setTuple[i][1])