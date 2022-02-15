def solution(brown, yellow):
    answer = []
    arr_b = []
    tot = brown + yellow

    for i in range(3, int((tot + 1)**0.5)+1):
        b_y = i # 세로
        for j in range(i, tot//i + 1):
            b_x = j # 가로
            if b_x * b_y == tot:
                if (b_x-2) * (b_y-2) == yellow:
                #arr_b.append([b_x, b_y])
                    answer.append(b_x)
                    answer.append(b_y)
                    break
                break
    #print(answer)
    return answer

brown = 50
yellow = 22
solution(brown, yellow)