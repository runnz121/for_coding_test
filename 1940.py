n = int(input())
m = int(input())
arr = list(map(int, input().split()))

check = [False] * n
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == m and check[i] == False and check[j] == False:
            check[i] = True
            check[j] = True
            cnt += 1

print(cnt)
