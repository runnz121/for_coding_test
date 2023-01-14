d, x = map(int, input().split())

# 첫째날
for i in range(1, 100000):
    tmp = [0] * 30
    tmp[0] = i
    # 둘째날
    for j in range(i + 1, 100000):
        tmp[1] = j

        for k in range(2, 30):
            tmp[k] = tmp[k-1] + tmp[k-2]
            if tmp[d - 1] == x:
                print(i)
                print(j)
                exit(0)