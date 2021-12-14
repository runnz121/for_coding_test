a, b = map(int, input().split())

mins = 1
for i in range(max(a,b),1,-1):
    if a % i == 0 and b % i == 0:
        mins = i
        break

amax = a//mins
bmax = b//mins
maxx = mins*amax*bmax

print(mins)
print(maxx)