arr = []
for i in range(30):
    x = str(input())
    arr.append(x)

arr.sort()

check = []

for i in range(1, 31):
    if str(i) not in arr:
        check.append(i)

check.sort()

for i in check:
    print(i)