
n, k = map(int, input().split())

cnt = 0

dp = [0] * n
dp[1] = 1

tmp = []

check = [False] * n

def back(depth):

    global tmp
    global cnt

    if depth == k:
        if sum(tmp) == n:
            cnt += 1
        return


    for i in range(n):
        if check[i]:
            continue

        tmp.append(i)
        #check[i] = True
        back(depth + 1)
        tmp.pop()
        #check[i] = False

back(0)

print(cnt + k)

# 20, 2

# 0 -> (0,0)                                        \\ 1
# 1 ->                   ||(1,0),(0,1)(k 갯수(0))    \\ 2
# 2 -> (1,1),            ||(2,0),(0,2)              \\ 3
# 3 -> (1,2),(2,1)       ||(0,3),(3,0)              \\ 4
# 4 -> (1,3),(3,1),(2,2) ||(4,0),(0,4)              \\ 5


# 6, 4

# 0 -> (0,0,0,0)
# 1 -> (1,0,0,0), (0,0,0,1), (0,1,0,0), (0,0,1,0)
# 2 -> (1,1,0,0), (0,0,1,1), (1,0,0,1), (0,1,1,0) ,