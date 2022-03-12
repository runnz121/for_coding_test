
n = int(input())

res = [[0, []] for _ in range(n + 1)]

res[1][0] = 0 # 최소값
res[1][1] = [1] # 누적 경로값

print(res)

for i in range(2, n + 1):

    # 여기서 현재 인덱스에서 -1 한 값을 정해주고 시작함
    res[i][0] = res[i-1][0] + 1
    res[i][1] = res[i-1][1] + [i]

    # 3으로 나누어 떨어지고, 3으로 나눈 인덱스의 값에 1더한게 현재 보다 작을때
    if i % 3 == 0 and res[i //3][0] + 1 < res[i][0]:
        res[i][0] = res[i // 3][0] + 1
        res[i][1] = res[i //3][1] + [i]

    if i % 2 == 0 and res[i // 2][0] + 1 < res[i][0]:
        res[i][0] = res[i // 2][0] + 1
        res[i][1] = res[i // 2][1] + [i]

print(res[n][0])
for i in res[n][1][::-1]:
    print(i, end = ' ')


stack =[1,2,3]
print(stack[-1])
