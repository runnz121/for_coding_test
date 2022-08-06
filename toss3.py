def solution(k, dungeons):

    answer = 0

    arr = []

    check = [False] * len(dungeons)

    def back(depth , end, k):

        nonlocal arr
        nonlocal answer

        if depth == end:
            tmp = 0
            for i in range(len(arr)):
                if arr[i][0] <= k:
                    k -= arr[i][1]
                    tmp += 1
                else:
                    break
            answer = max(tmp, answer)
            return

        for i in range(len(dungeons)):
            if check[i]:
                continue
            arr.append(dungeons[i])
            check[i] = True
            back(depth + 1, end, k)
            check[i] = False
            arr.pop()

    for p in range(1, len(dungeons)+1):
        back(0, p, k)

    return answer

print(solution(80 ,[[80, 20], [50, 40], [30, 10]]))