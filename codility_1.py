def solution(N):
    ans = ''
    cnt = 0
    flag = False

    answer = 0

    def recur(N):
        nonlocal ans

        if N == 1:
            ans = str(N) + ans
            return

        res = N % 2
        div = N // 2
        ans = str(res) + ans
        recur(div)

    recur(N)


    for i in ans:
        if i == '1' and flag == False:
            flag = True

        if flag == True and i == '0':
            cnt += 1

        if i == '1' and flag == True:
            answer = max(answer, cnt)
            cnt = 0


solution(1041)
