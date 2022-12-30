x = str(input().split())

arr = ['a', 'e', 'i', 'o', 'u']

cnt = 0
for i in x :
    if i in arr:
        cnt += 1
print(cnt)