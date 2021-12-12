n = int(input())

count = 0
arr = [0] * n
def check(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x-i: # 대각선과, 상하좌우가 같으면 안됨
            return False
    return True


def queen(x):
    global count
    if n == x:
        count += 1
        return

    for i in range(n):
        arr[x] = i # 해당 열에 i 번째에 퀸이 존재하는 경우(8번씩 번갈아가면서 들어감)
        if check(x): #체크 함수를 통과하면
            queen(x+1) # 다음 열에서 퀸의 위치를 고려함
queen(0)
print(count)

# 각 열(row)마다 퀸이 무조건 한개씩 존재
# 퀸이 올 수 없는 조건은, 각 열에 대해서 상하좌우, 그리고 대각선 은 올 수 없음
# 배열안에 각 열에 해당하는 퀸의 x 좌표를 넣고 이것을 재귀로 돌림
# https://claude-u.tistory.com/245