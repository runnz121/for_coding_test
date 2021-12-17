from collections import deque
import sys

# 여
while True:
    ans = 'yes'
    strs = sys.stdin.readline()[:-1]
    if strs == '.':
        break

    stack = deque()
    for i in strs:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if len(stack) == 0:
                ans = 'no'
                break
            res = stack.pop()
            #print('res',res)
            if res != '(':
                ans = 'no'
                break
        elif i == ']':
            if len(stack) == 0:
                ans = 'no'
                break
            res = stack.pop()
            if res != '[':
                ans = 'no'
                break
    #모든 검색 끝냈을때 큐가 비어있는지 확인해주어야 함
    if len(stack) != 0:
        ans = 'no'
    print(ans)
