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
        # 끝이 I로 끝났을 경우 1 더해줌
        if flag == False:
            tmp += 1
        check.append(tmp)
        tmp = 0
    if i == m-1:
        check.append(tmp)

for k in check:
    # 크거나 같은 것들 중에서(길이가)
    if k >= lens - 1:
        # 비교열 길이 빼고 I, O 2종류 문자만 있음으로 2로 나눠준 후 맨 마지막 반환 가능한 갯수 1을 더해줘서 계산
        cnt += ((k - lens) // 2 + 1)
# print(lens)
# print(check)
print(cnt)
