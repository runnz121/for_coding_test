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

#유클리드 호제법으로 최대공약수 고하기
def get_gcd(a, b):
    while b != 0:
        d = a % b # 나머지
        a = b # 두번째  => 첫번째
        b = d # 나머지 => 두번째
    return a

# 이웃한 숫자의 차이 구하기
for p1, p2 in zip(arr, arr[1:]):
    res = abs(p1-p2)
    gcd.append(res)

# 각 숫자 차이의 최대 공약수 구하기
ggg = gcd[0]
for i in range(1, len(gcd)):
    ggg = get_gcd(gcd[i], ggg)


result = []
for i in range(2, int(ggg ** 0.5)+1): #최대공약수의 제곱근만큼만 돌림
    if ggg % i == 0 :# 약수 찾기
        result.append(i)
        result.append(ggg//i) # 24약수를 찾을때 i가 2이면 12도 추가해야함
result.append(ggg) # 해당 최대공약수 값도 약수 임으로 넣어줌
result.sort()
print(*set(result)) # 중복 제거로 set (list unpacking시 사용)

# gcd_a = int(max(gcd) ** 0.5)
# print("1", gcd_a)
# print("gcd", gcd)
# gcd.sort()
# ans = []
# for i in range(1, gcd_a + 1):
#     for j in gcd:
#         if j % i == 0:
#             ans.append(i)
#             ans.append(j//i)
# print("2",ans)
# ans1 = []
# for k in ans:
#     if ans.count(k) == T-1:
#         ans1.append(k)
# print("3",ans1)
# set(ans1)
# ans1.sort()
# print(' '.join(map(str, set(ans1))))