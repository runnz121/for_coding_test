import sys
import copy

input = sys.stdin.readline

team = str(input().rstrip())
num = int(input())

arr = []
for i in range(num):
    x = str(input().rstrip())
    arr.append(x)

db = dict()

for str in arr:
    if str[0] in db:
        db[str[0]] += 1
    else:
        db[str[0]] = 1

max_num = 1
flag = False
team = set(team)
for key in team:
    if db[key]:
        flag = True
        max_num *= db[key]

if not flag:
    print(0)
else:
    print(max_num)