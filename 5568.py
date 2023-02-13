import copy

n = int(input())
k = int(input())

arr = []

for i in range(n):
    x = str(input())
    arr.append(x)

tmp = []
tmp1 = []
res = []
check = [False] * n

def back(depth):

    global tmp
    global tmp1
    global res

    if depth == k:
        tmp1 = copy.deepcopy(tmp)
        res.append(tmp1)
        return

    for i in range(n):
        if not check[i]:
            check[i] = True
            tmp.append(arr[i])
            back(depth + 1)
            check[i] = False
            tmp.pop()
back(0)

resToInt = []
for idx in res:
    nums = ''.join(idx)
    resToInt.append(int(nums))

resToInt = set(resToInt)
print(len(resToInt))