N, K = map(int, input().split())


arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()

#1~최대 수
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    # 배열안에수를 각각 나눠주고 그것의 몫을 더해줌
    for i in arr:
        lines += i//mid
    # 라인이 주어진 수보다 크다면
    if lines >= K:
        start = mid + 1
    else:
        end = mid - 1
print(end)