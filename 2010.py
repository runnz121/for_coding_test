n = int(input())

con = []
for i in range(n):
    x = int(input())
    con.append(x)

con.sort(reverse=True)

sums = con[0]

for k in range(1, n):
    sums += con[k]-1

print(sums)