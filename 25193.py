n = int(input())

x = list(str(input()))

c_cnt = 0
for i in range(n):
    if x[i] == 'C':
        c_cnt += 1

rest = n-c_cnt + 1

# 올림 처리
add = c_cnt%rest
# 나눠 떨어지는게 아니면 1을 더해주고 아니면 0
if add != 0:
    add = 1
else:
    add = 0

if rest == 0:
    print(n)
else:
    print(c_cnt//rest + add)