def solution(num):
    cnt = 0
    for i in range(num+1):
        for j in range(60):
            for z in range(60):
                if '3' in str(i) + str(j) + str(z):
                    cnt += 1

    print(cnt)
    return cnt



solution(5)