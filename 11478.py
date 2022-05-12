arr = str(input())

ans = []

for i in range(1, len(arr) + 1): # 몇게씩 할지
    for j in range(len(arr)):
        ans.append(arr[j:j+i])

print(len(set(ans)))