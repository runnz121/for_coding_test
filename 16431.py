
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())

enum1 = "bessie"
enum2 = "daisy"
enum3 = "tie"

mins = min(d1, d2)
maxx = max(b1, b2)

# 대각선 이동이 가능함으로 가로세로중 더 긴것이 이동거리
dist1 = max(abs(d1-b1) , abs(d2-b2))
dist2 = abs(c1 - d1) + abs(c2 - d2)


if dist1 < dist2:
    print(enum1)
elif dist1 > dist2:
    print(enum2)
else:
    print(enum3)