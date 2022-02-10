a, b = map(int, input().split())

arr = list(map(int, input().split()))

def dfs(idx, sum):
    global cnt
    # 인덱스가 주어진 값보다 커지면 종료
    if idx >= a:
        return
    # 배열의 원소값을 더해서
    sum += arr[idx]

    #주어진 조건에 만족하면 카운트 1
    if sum == b:
        cnt += 1

    # 현재 인덱스의 값을 포함하지 않는 것
    dfs(idx + 1, sum-arr[idx])

    # 현재 인덱스의 값을 포함한것
    dfs(idx + 1, sum)
cnt = 0
dfs(0,0)
print(cnt)