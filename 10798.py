arr = [[""] * 15 for _ in range(5)]

res = ""
for i in range(5):
    ss = list(str(input()))
    for x in range(len(ss)):
        arr[i][x] = ss[x]

for x in range(15):
    for y in range(5):
        if arr[y][x] != "":
            res += arr[y][x]

print(res)

for pair in zip(arr[0], arr[1], arr[2], arr[3], arr[4]):
    print(pair)