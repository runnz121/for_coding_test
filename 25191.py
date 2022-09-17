n = int(input())

a,b = map(int, input().split())

maxa = a//2

print(min(maxa + b, n))