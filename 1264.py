
arr = ['A','E','I','O','U']
while True:
    x = str(input())
    x = x.upper()
    if x == '#':
        break
    count = 0
    for i in x:
        if i.upper() in arr:
            count += 1
    print(count)
