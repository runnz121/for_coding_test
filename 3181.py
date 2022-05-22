excludes = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

find = list(map(str, input().split()))

ans = ''
ans += find[0][0:1].upper()
for idx in range(1, len(find)):
    if find[idx] not in excludes:
        ans += find[idx][0:1].upper()

print(ans)