n = int(input())

def sums(lists):
    tot = 0
    for i in lists:
        if i.isdigit():
            tot += int(i)
    return tot

arr = []

for k in range(n):
    lis = input()
    arr.append(lis)

arr.sort(key = lambda x : (len(x), sums(x), x))

for k in arr:
    print(k)