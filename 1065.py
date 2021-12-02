n = int(input())

ans = 0
if n <= 99:
    ans = n
else:
    for j in range(100, n+1):
        j = str(j)
        a = int(j[0])
        b = int(j[1])
        c = int(j[2])
        if c - b == b - a:
            ans += 1
            print("first",a, b, c)
        elif a - b == b - c:
            ans += 1
            print("sec", a, b, c)
    ans += 99
print(ans)

# 100 보다 작으면 99개 무조건 출력,
# 100이상일 경우 각 자리수를 str -> int로 변환하여 앞에서 뒤로, 뒤에서 앞으로 각각 경우의 수 고려하고
# elif 조건 주어서 중복 제거
