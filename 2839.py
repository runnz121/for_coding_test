n = int(input())

min_value = 1e9
for j in range(1000):
    for i in range(2000):
        if n == ((3 * j) + (5 * i)): # 1씩 돌리면서 전체 탐색
            min_value = min(min_value, i+j)
if min_value == 1e9: # min value 값 변동이 없으면 답이 없다는 뜻임으로 -1 출력
    min_value = -1
print(min_value)