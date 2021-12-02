import sys
input = sys.stdin.readline

n = int(input())
arr = []
checklist = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for a in range(n):
    students = arr[a][0]
    sums = 0
    above = 0
    for b in range(1, len(arr[a])):
        sums += arr[a][b]
    average = round(sums/students, 5)
    for c in range(1, len(arr[a])):
        if arr[a][c] > average:
            above += 1
    ss = round(above/students * 100, 3)
    print(f'{ss:.3f}%')
