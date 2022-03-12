import sys

input = sys.stdin.readline

def dfs(idx, cnt):
    global ans
   # print(select) #-> 이부분을 출력하면 체크배열이 어떤식으로 동작하는지 알 수 있음

    # 팀으로 나뉠 만큼 나눠저야 실행
    if cnt == n // 2:
        start, link = 0, 0

        for i in range(n): # 0 1 2 3
            for j in range(n): # 0 1 2 3

                # 0,0 부터 시작했을시 현재 , i = 0,1  는 선택되어 있음으로 팀이 구분이됨
                if select[i] and select[j]: # 0,0 // 0,1 // 1,0 // 1,1
                    start += a[i][j]

                # i = 2,3 은 안 선택되어있음으로 해당 값을 더해줌
                elif not select[i] and not select[j]: # 2,2 // 2,3 // 3,2 // 3,3
                    link += a[i][j]
  
        # 최소값을 구함
        ans = min(ans, abs(start - link))

    for i in range(idx, n):
        if select[i]:
            continue

# 이 부분이 핵심 -> 이전 dfs가 종료되기 전까지 select[i]는 계속 1이다
        select[i] = 1
        dfs(i + 1, cnt + 1)
        select[i] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


# 체크배열 (팀 구분을 위함)
select = [0 for _ in range(n)]
ans = sys.maxsize
dfs(0, 0)
print(ans)