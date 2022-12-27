a, b = map(int, input().split())

pascal = []
pascal.append([1])
pascal.append([1,1])

for i in range(3, 31):
    tmp = [1] * i
    for k in range(1, i-1):
        tmp[k] = pascal[i-2][k-1] + pascal[i-2][k]
    pascal.append(tmp)

print(pascal[a-1][b-1])