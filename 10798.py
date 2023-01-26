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