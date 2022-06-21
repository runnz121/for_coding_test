n = int(input())

arr = []

for i in range(n):
    x = input()
    if len(x) >= 2:
        k = list(x)
        print(k[0] + k[len(x)-1])
    else:
        k = list(x)
        print(k[0]+k[0])