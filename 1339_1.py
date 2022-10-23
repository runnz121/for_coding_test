import copy
import sys

input = sys.stdin.readline

n = int(input())
arr = []
db = set()

for i in range(n):
    x = str(input().rstrip())
    arr.append(x)
    x_list = list(x)

    for k in x_list:
        db.add(k)
db = list(db)
db.sort()


number = [i for i in range(9, 9-len(db), -1)]

check = [False] * (len(db))
numbers_arr = []
tmp = []
def back(depth):

    global numbers_arr
    global tmp

    tmp1 = copy.deepcopy(tmp)

    if depth == len(db):
        numbers_arr.append(tmp1)
        return

    for i in range(len(db)):
        if check[i]:
            continue

        tmp.append(number[i])
        check[i] = True
        back(depth + 1)
        check[i] = False
        tmp.pop()
back(0)

for idx in numbers_arr:
