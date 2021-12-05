arrx = []
arry = []
ans = ""
for i in range(3):
    a, b = map(int, input().split())
    arrx.append(a)
    arry.append(b)

# 각 x, y 배열에 담고 카운트 세어서 한개일 경우 출력
for i in range(3):
    if arrx.count(arrx[i]) == 1:
        x = arrx[i]
    if arry.count(arry[i]) == 1:
        y = arry[i]
print(f"{x} {y}")
