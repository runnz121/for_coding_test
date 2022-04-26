x, y = map(int, input().split())

m = int(y ** 0.5)  # 루트 값까지만 돌음
sieve = [True] * y

for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i + i, y, i):
            sieve[j] = False

ans = [i for i in range(2, y) if sieve[i] == True]

answer = 0
for k in range(x, y+1):
    x = 0
    cnt = 0
    while k > 1:
        start = ans[x]
        if k % start == 0:
            k = k//start
            cnt += 1
        else:
            x += 1
        if x >= len(ans):
            break
    if cnt in ans:
        answer += 1

print(answer)

