import math

a, b = map(int, input().split())

arr = [True] * (b+1)

#n 제곱근까지만 확인
for i in range(2, int(math.sqrt(b)) + 1):
    if arr[i] == True:# 아직

        j = 2#2, 3 제외
        while i * j <= b: # 최대수보다 작을 동안 j 증가시키며 배수로 돌리고 해당 값을 false로 치환(소수가 아님으로)
            arr[i * j] = False
            j += 1

#남은 arr의 true는 소수임으로 해당 값만 출력
for i in range(a, b+1):
    if i != 1 and arr[i] == True:
        print(i)