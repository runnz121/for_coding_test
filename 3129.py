a = list(str(input()))
b = list(str(input()))

if len(a) != len(b):
    idx = 0
    while len(a) >= len(b):
        b.append(b[idx])
        idx += 1

ans = ''
for idx in range(len(a)):
    sums = (ord(a[idx])-97) - (ord(b[idx])-97)
    print(sums)
    if sums < 0:
        ans += chr(26 + sums + 97)
    else:
        ans += chr(sums + 97)

print(ans)