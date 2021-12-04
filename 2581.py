a = int(input())
b = int(input())

arr= []
check = []

for i in range(a, b+1):
    for j in range(1, i+1):
        if i % j == 0: #나누서ㅓ 0이면 체크 배열에 넣음
            check.append(j)
    if 2 <= len(check) < 3: # 체크베열 갯수가 2개이면 해당 수는 소수
        arr.append(i)
    check = [] #초기화

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))