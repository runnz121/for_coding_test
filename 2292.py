n = int(input())

db = dict()
#166666667
db[0] = 1
if n == 1:
    print(1)
else:
    for i in range(1, 1000000000):
        db[i] = db[i-1] + 6*i
        if db[i] >= n:
            ans = i + 1
            break
    print(ans)

# db[0] = 1 1
# db[1] = 2,3,4,5,6,7 6
# db[2] = 8,9,10,11,12,13,14,15,16,17,18,19 12
# db[3] = 20~37 18
# db[4] = 38~61 24