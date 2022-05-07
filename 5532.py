l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())


for i in range(l):
    if c * i >= a and d * i >= b:
        print(l - i)
        exit()