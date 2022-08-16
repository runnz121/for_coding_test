import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
p = str(input())

init = 'IOI'

init += 'OI' * (n-1)

lens = 3 + (n-1) * 2

lent = lens//2 + 1

cnt = 0

tmp = 0

flag = True

check = []

for i in range(m):
    if p[i] == 'I' and flag == True:
        tmp += 1
        flag = False

    elif p[i] == 'O' and flag == False:
        tmp += 1
        flag = True

    else:
        if flag == False:
            tmp += 1
        check.append(tmp)
        tmp = 0
    if i == m-1:
        check.append(tmp)

for k in check:
    # 크거나 같은 것들 중에서(길이가)
    if k >= lens - 1:
        cnt += ((k - lens) // 2 + 1)
# print(lens)
# print(check)
print(cnt)
