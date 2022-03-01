n, m = map(int, input().split())

k = 1
for i in range(n,n-m,-1):
    k *= i
x = 1
for j in range(1,m+1):
    x *= j

print(k//x)