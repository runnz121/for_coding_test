x = list(str(input()))


stack = []
stick = 0
cut = 0
total = 0

for i in range(len(x)):
    if x[i] == '(':
        stack.append(x[i])
    else:
        if x[i-1] == '(':
            stack.pop()
            total += len(stack)
        else:
            stack.pop()
            total += 1


print(total)