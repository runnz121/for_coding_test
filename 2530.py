h, m, s = map(int, input().split())
mins = int(input())

mm = mins//60
ss = mins%60

s = s + ss
if s >= 60:
    m += s // 60
    s = s%60

m = m + mm
if m >= 60:
    h += m // 60
    m = m%60

if h >= 24:
    if h == 24:
        h = 0
    else:
        h = h%24


print(h, m, s)
