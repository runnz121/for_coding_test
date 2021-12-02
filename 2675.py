n = int(input())
arr =[]

for _ in range(n):
    arr.append(input().split())


for i in range(len(arr)):
    repeat = int(arr[i][0])
    ans = ""
    for j in range(len(arr[i][1])):
        ans += arr[i][1][j]*repeat
    print(ans)

# 빈 값 주고 반복문 돌림