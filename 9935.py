import sys

input = sys.stdin.readline

string = str(input().rstrip())
comp = str(input().rstrip())

stack = []

for i in range(len(string)):
    stack.append(string[i])

    if len(stack) >= len(comp):
        tmp = "".join(stack[-len(comp):])
        if tmp == comp:
            cnt = 0
            while cnt < len(comp):
                stack.pop()
                cnt += 1
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))