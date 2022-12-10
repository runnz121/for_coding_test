arr = []
for i in range(9):
    x = list(map(int, input().split()))
    arr.append(x)

ans = -1
ans_arr = [0, 0]
for i in range(9):
    for j in range(9):
        if arr[i][j] > ans:
            ans = arr[i][j]
            ans_arr[0] = i + 1
            ans_arr[1] = j + 1

print(ans)
print(*ans_arr)
