T = int(input())

arr = []
for i in range(T):
    arr.append(list(map(int, input().split())))

for i in arr:
    a = i[0]
    b = i[1]
    mins = 1
    for i in range(max(a,b),1,-1):
        if a % i == 0 and b % i == 0:
            mins = i
            break

    amax = a//mins
    bmax = b//mins
    maxx = mins*amax*bmax
    print(maxx)
