x = str(input())

ans = ''

for i in x:
    if i.islower():
        ans += i.upper()
    else:
        ans += i.lower()

print(ans)