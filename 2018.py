n = int(input())

ans = 0
sums = 0
for i in range(1, n+1):
    sums += i
    if n-sums >= 0 and (n-sums)%i == 0:
        ans += 1

print(ans)