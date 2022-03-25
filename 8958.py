import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    string = list(str(input().rstrip()))

    sum = 0
    temp = 0
    for i in range(len(string)):
        if string[i] == 'O':
            temp += 1
            sum += temp
        else:
            temp = 0
    print(sum)