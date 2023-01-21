a = list(input())
b = list(input())

aa, bb = a[:], b[:]

a1 = [x for x in a if not x in bb or bb.remove(x)]
b1 = [x for x in b if not x in aa or aa.remove(x)]

print(len(a1) + len(b1))