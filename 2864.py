n, m = map(str, input().split())

n1 = n.replace('5','6')
m1 = m.replace('5','6')

maxs = int(n1) + int(m1)

n2 = n.replace('6','5')
m2 = m.replace('6','5')

mins = int(n2) + int(m2)

print(mins, maxs)