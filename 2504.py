# bracket = list(input())
#
# stack = []
# answer = 0
# tmp = 1
#
# for i in range(len(bracket)):
#
#     if bracket[i] == "(":
#         stack.append(bracket[i])
#         tmp *= 2
#
#     elif bracket[i] == "[":
#         stack.append(bracket[i])
#         tmp *= 3
#
#     elif bracket[i] == ")":
#         if not stack or stack[-1] == "[":
#             answer = 0
#             break
#         if bracket[i-1] == "(":
#             answer += tmp
#         stack.pop()
#         tmp //= 2
#
#     else:
#         if not stack or stack[-1] == "(":
#             answer = 0
#             break
#         if bracket[i-1] == "[":
#             answer += tmp
#
#         stack.pop()
#         tmp //= 3
#
# if stack:
#     print(0)
# else:
#     print(answer)
########################################################(스택에 숫자를 넣어서 계산)
import sys

str = sys.stdin.readline().rstrip()

stack = list()

for i in str:
    print(stack)

    if i == ")":
        temp = 0

        while stack:
            top = stack.pop()
            if top == "(":
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            elif top == "[":
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)

    elif i == "]":
        temp = 0

        while stack:
            top = stack.pop()
            if top == "[":
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif top == "(":
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)

    else:
        stack.append(i)

result = 0

for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        result += i

print(result)