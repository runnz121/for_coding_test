import sys
T = int(input())

arr = []
stack = []
for _ in range(T):
    arr.append(str(input()))

for i in range(T):
    arr[i] = arr[i].split(' ')

    if arr[i][0] == 'push':
        stack.append(int(arr[i][1]))
    elif arr[i][0] == 'top':
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)
        #print(stack)
    elif arr[i][0] == 'size':
        print(len(stack))
    elif arr[i][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif arr[i][0] == 'pop':
        if len(stack) >= 1:
            pops = stack.pop()
            print(int(pops))
        else:
            print(-1)

