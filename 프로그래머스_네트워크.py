from collections import deque

def solution(n, computers):
    answer = 0

    def dfs(x, y):
        if computers[x][y] == 0:
            return

        # 이미 여기서 0으로 만들어서 나 자신 들어가도 상관없음
        computers[x][y] = 0

        # 해당 y 배열을 전체 탐색
        for i in range(n):
            if computers[y][i] == 1 :
                dfs(y,i)

    for i in range(n):
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                dfs(i,j)
               # print(computers)
                answer += 1

   # print(answer)
    return answer


computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n = 3
solution(n, computers)
