x, y = map(int, input().split())
k = int(input())

ups = (y + k)//60

if y + k >= 60:
    mins = (y+k) - (ups*60)
else:
    mins = y+k

if ups >= 1:
    hos = x + ups
else:
    hos = x

if hos >= 24:
    hos = hos - 24

print(hos,mins)