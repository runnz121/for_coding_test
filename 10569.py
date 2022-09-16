n = int(input())

for i in range(n):
    v, e = map(int, input().split())
    print(2 - v + e)