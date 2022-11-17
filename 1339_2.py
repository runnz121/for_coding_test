import sys

input = sys.stdin.readline
alpha = []
db = {}
numList = []

n = int(input())

for i in range(n):
    x = str(input().rstrip())
    alpha.append(x)


for i in range(n):
    for j in range(len(alpha[i])):
        if alpha[i][j] not in db:
            db[alpha[i][j]] = 10 ** (len(alpha[i]) - j - 1)
        else:
            db[alpha[i][j]] += 10 ** (len(alpha[i]) - j - 1)


for value in db.values():
    numList.append(value)

numList.sort(reverse=True)


ans = 0
for i in range(9, 9-len(numList), -1):
    ans += i * numList[9-i]

print(ans)