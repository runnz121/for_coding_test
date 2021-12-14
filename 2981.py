import sys, math
T = int(sys.stdin.readline())

arr = []
gcd = []

for i in range(T):
    arr.append(int(sys.stdin.readline()))

# a, b, c, d 에서
# a-b, b-c, c-d의 최대공약수를 구하면 된다
# X0 = a * t + r
# X1 = b * t + r
# X1 - X0 = (b - a) * t
# 각 수를 빼면 나머지는 자동적으로 사라짐
# 즉 각 수의 델타 값이 최대공약수의 배수가 됨
# 따라서 이 수도 gcd의 배수 혹은 약수가 됨

for p1, p2 in zip(arr, arr[1:]):
    res = abs(p1-p2)
    gcd.append(res)
gcd_a = int(max(gcd) ** 0.5)
print("1", gcd_a)
print("gcd", gcd)
gcd.sort()
ans = []
for i in range(1, gcd_a + 1):
    for j in gcd:
        if j % i == 0:
            ans.append(i)
            ans.append(j//i)
print("2",ans)
ans1 = []
for k in ans:
    if ans.count(k) == T-1:
        ans1.append(k)
print("3",ans1)
set(ans1)
ans1.sort()
print(' '.join(map(str, set(ans1))))