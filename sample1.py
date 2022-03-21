arr = [['A', 'B'], ['A', 'B'],['A', 'C'],['A', 'D'],['Z', 'A'],['A', 'B'],['A', 'B'],['C', 'B']]

res = sorted(arr, key = lambda x: x[0])

print(res)

db = dict()

duple = []

for i in res:
    if i not in duple:
        duple.append(i)

print(duple)
for i in duple:
    if i[1] < i[0]:
        i[0], i[1] = i[1], i[0]

print(duple)