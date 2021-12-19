x = int(input())
case = list(map(int, input().split()))
#증가 하는 갯수 담음
increase = [1 for i in range(x)]

for i in range(x):
    for j in range(i): #이전 수의 범위까지만 확인
        # 해당 범위안에서 비교하며, 해당 범위 숫자보다 크다면
        if case[i] > case[j]:
            # 현재 범위까지의 수들중에서 최고로 긴 증가 수열의 갯수에다가 1을 더한 값을 현재 인덱스 dp 에 저장
            increase[i] = max(increase[i], increase[j]+1)

#감소하는 갯수 담음
decrease2 = [1 for i in range(x)]
for i in range(x-1, -1, -1):
    for j in range(x-1, i, -1):
        if case[i] > case[j]:
            decrease2[i] = max(decrease2[i], decrease2[j]+1)

#위의 두 수열의 값을 더하고, 현재 인덱스에 해당하는 값은 중복됨으로 하나 빼줌
result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease2[i] -1 

print(max(result))