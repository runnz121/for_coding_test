T = int(input())

arr = []

for i in range(T):
    arr.append(list(map(int, input().split())))

#arr[i][1], arr[i][0]
def recur1(M, N):
    if N == 0:
        return 1
    return M * recur1(M-1, N-1)

#팩토리얼 계산
def recur2(M):
    if M == 1:
        return 1
    return M * recur2(M-1)

i = 0
while i < T:
    div = recur1(arr[i][1], arr[i][0])
    mod = recur2(arr[i][0])
    print(div//mod)
    i+=1