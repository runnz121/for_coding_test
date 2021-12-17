import sys
from collections import deque

T = int(sys.stdin.readline())

stack = deque()
arr = []
ansArr = []
oper = []

for _ in range(T):
    ins = int(input())
    arr.append(ins)

if arr[0] == 1:
    ans = 'no'

# 스택 초기화(최초 출력 숫자까지 값을 넣어줌)
for i in range(1, arr[0]+1):
    stack.append(i)
    oper.append('+')

# 맨 처음 숫자 빼줌
res = stack.pop()
ansArr.append(res)
oper.append('-')

# 이미 스택에 들어가 있는 숫자 다시 않넣기 위해 최대값 지정
max_val = arr[0]
for i in range(1, len(arr[1:])):
    # 수열 들어있는 배열에서 이전것이 더 큰 경우
    if arr[i] < arr[i-1] and arr[i] < max_val:
        # 빼줌
            res1 = stack.pop()
            ansArr.append(res1)
            oper.append('-')
    elif arr[i] > arr[i-1]:
        # 그게 아니라면 다음 큰 숫자까지 값을 스택에 넣어주고
        for k in range(max_val+1, arr[i]+1):
            stack.append(k)
            oper.append('+')
        # 맨 최대값을 스택에서 빼줌
        res1 = stack.pop()
        oper.append('-')
        ansArr.append(res1)
        max_val = arr[i] #최대값 갱신
# 큐나머지가 있는지 확인하고 있으면 큐 비워줌
if len(stack) > 0:
    res1 = stack.pop()
    ansArr.append(res1)
    oper.append('-')

# 출력 분기
flag = 0
for k in range(T):
    if ansArr[k] != arr[k]:
        flag = 1

if flag == 1:
    print('NO')
else:
    for x in oper:
        print(x)

#
# print('stack',stack)
# print('ansArr',ansArr)
# print('oper', oper)