n = int(input())

onlyNum = []
strNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(n):
    x = list(str(input()))
    one = ''
    flag = True
    for k in range(len(x)):
        if x[k] == '0' and k == len(x) - 1 and x[k - 1] not in strNum:
            onlyNum.append('0')
        elif x[k] in strNum:
            one += x[k]
            if k == len(x) - 1:
                onlyNum.append(one)
        else:
            onlyNum.append(one)
            one = ''
ans = []
#print(onlyNum)
for i in onlyNum:
    if i != '':
        ans.append(int(i))
ans.sort()

for x in ans:
    print(x)
