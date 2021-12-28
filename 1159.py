from collections import Counter

T = int(input())

arr = []
first = []
ss = ''

for i in range(T):
    arr.append(str(input()))

for i in range(T):
    first.append(arr[i][0])

ans = Counter(first)
# print(ans.keys(), ans.values())

ans = dict(ans)
print(ans)

for i in ans.items():
    if i[1] >= 5:
        ss += i[0]
if len(ss) == 0:
    print("PREDAJA")
else:
    print(ss)


# li = sorted([input()[0] for _ in range(int(input()))])
# s = set(li)
# res = []
# for c in s:
#     if li.count(c) >= 5:
#         res.append(c)
# print(''.join(sorted(res)) if len(res) > 0 else "PREDAJA")