x = list(str(input()))

height = 10

for i in range(1, len(x)):
    if x[i - 1] == '(' and x[i] == ')':
        height += 10
    elif x[i - 1] == '(' and x[i] == '(':
        height += 5
    elif x[i - 1] == ')' and x[i] == ')':
        height += 5
    else:
        height += 10

print(height)