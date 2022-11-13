arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
cnt3 = 0
db = {0:'E', 1:'A',2:'B',3:'C',4:'D'}
for i in arr1:
    if i == 0:
        cnt1 += 1
print(db[cnt1])
for i in arr2:
    if i == 0:
        cnt2 += 1
print(db[cnt2])
for i in arr3:
    if i == 0:
        cnt3 += 1
print(db[cnt3])

