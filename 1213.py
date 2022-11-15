import math
import sys

input = sys.stdin.readline

x = str(input().rstrip())

impossible = "I'm Sorry Hansoo"

x = list(x)

db = dict()

for i in range(len(x)):
    if x[i] in db:
        db[x[i]] += 1
    else:
        db[x[i]] = 1

answer = ''
not_valid_cnt = 0
for i in db.keys():
    if db[i] % 2 != 0:
        answer += i
        db[i] -= 1
        not_valid_cnt += 1

if not_valid_cnt > 1:
    print(impossible)
    exit(0)

db = sorted(db.items(), key=lambda x: x[0])

front = ''
for key, value in db:
    front += round(value / 2) * key

back = front[::-1]

print(front + answer + back)
