import sys
from collections import deque
T = int(input())

while T > 0:
    stack = deque()
    flag = 0
    ans = 'NO'
    strs = list(map(str, sys.stdin.readline()[:-1]))
    for i in range(len(strs)):
        if strs[i] == '(':
            flag += 1
            stack.append(strs[i])
        elif strs[i] == ')':
            flag -= 1
            if len(stack) == 0:
                ans = 'NO'
                break
            else:
                stack.popleft()
    if flag == 0 and len(stack) == 0:
        ans = 'YES'
    print(ans)
    T -= 1