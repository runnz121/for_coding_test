x = int(input())

lists = list(str(x))


ans = 0
for i in range(len(lists)):
    if lists[i] == '0':
        if lists[i-1] != '0' or i > 0:
            ans -= int(lists[i - 1])
            strs = lists[i-1] + '0'
            ans += int(strs)
    else:
        ans += int(lists[i])

print(ans)