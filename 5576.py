a = []
for i in range(10):
    a.append(int(input()))
b = []
for j in range(10):
    b.append(int(input()))

a.sort(reverse=True)
b.sort(reverse=True)

print(sum(a[:3]), sum(b[:3]))
