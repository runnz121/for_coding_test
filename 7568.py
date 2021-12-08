import sys
cnt = int(sys.stdin.readline())
arr = []
#모든 수 입력받기
for i in range(cnt):
    arr.append(list(map(int, sys.stdin.readline().split())))

#랭크를 어펜드함

for a in range(len(arr)):
    rank = 1
    std1 = arr[a][0]
    std2 = arr[a][1]
    for j in range(len(arr)):
        if arr[j][0] > std1:
            if arr[j][1] > std2:
                rank +=1
    arr[a].append(rank)

for x in range(len(arr)):
    print(arr[x][2], end= ' ')