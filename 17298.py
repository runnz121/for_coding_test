import copy
import sys
from collections import deque

T = int(input())
stack = deque() #원소의 인덱스를 넣어주는 목적
arr = list(map(int, sys.stdin.readline().split()))
# -1로 초기화
ans = [-1] * T

#처음 스택엔 0 이 들어가 있음
stack.append(0)
for i in range(1, T):
    # stack의  -1은 0이다. 따라서  0 < arr[1] 값을 비교함
    # while 문에서 스택에 값이 존재하고, 스택에서 인덱스를 거꾸로 꺼내면서
    # 현재 인덱스에 해당하는 arr 값이랑 비교해서
    # 현재 arr 값이 더 크면, 이전의 인덱스 값도 모두 현재 인덱스 값으로 넣으면 된다
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i] # 스택에서 해당 인덱스에 해당하는 ans 배열의 값을 큰 값으로 변경
    stack.append(i) # 스택에 인덱스를 추가
   # print(i, stack, arr[stack[-1]], stack[-1], arr[i])

print(*ans)