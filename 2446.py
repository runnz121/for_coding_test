import re
n = int(input())

for i in range(n*2-1, -1, -2):
    if i == 1:
        print((n * 2 - i) // 2 * " " + i * "*", end= "")
    else:
        print((n*2-i)//2*" " + i*"*")
print()

for i in range(-1, n*2, 2):
    if i == -1 or i == 1:
        continue
    else:
        print((n*2-i)//2*" " + i*"*")
