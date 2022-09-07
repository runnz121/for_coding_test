n, m = map(int, input().split())

r, c, d = map(int, input().split())

# 바라보는 방향 : 북, 동, 남, 서
dd = [0,1,2,3]
graph = []

# 현재 바라보고 있는 방향
curr_direction = d
# 현재 위치
curr_location = [r, c]

# 데이터 입력
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

# 1. 현재 위치 청소
def check1(x, y):
    if graph[x][y] == 0:
        graph[x][y] = -1

# 2.1 왼쪽방향에 청소하지 않은 공간이 있다면 회전 후 전진 -> 청소
def check2(x, y):
    if graph[x][y-1] == 0:
        curr_direction = dd[d-1]




def main():
