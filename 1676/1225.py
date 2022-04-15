a, b = map(int, input().split())

a, b = str(a), str(b)

arr = []

answer = 0

for i in a:
    for j in b:
        answer += int(i) * int(j)

print(answer)