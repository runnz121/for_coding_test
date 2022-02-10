x = int(input())

cnt = 0

graph = [True] * (x+1)

m = int ((x+1) **0.5)

for i in range(2, m+1):
    if graph[i]:
        for j in range(i+i, (1+x), i):
            graph[j] = False

odd = [i for i in range(2, (x+1)) if graph[i] == True]


start = 0
end = 0
sums = 0
while True:
    if sums >= x:
        sums -= odd[start]
        start += 1
    else:
        if end == len(odd):
            break
        else:
            sums += odd[end]
            end += 1


    if sums == x:
        cnt += 1

print(cnt)