n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

shark_big = 2

def check()