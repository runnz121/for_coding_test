n = int(input())

for i in range(n):
    x = list(map(int, input().split()))

    x.sort()

    x = x[1:len(x)-1]

    if x[len(x)-1] - x[0] >=4:
        print('KIN')
    else:
        print(sum(x))