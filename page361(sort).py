def solution(N, stages):
    answer = []
    length = len(stages)

    #스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        #해당 스테이지에 머물러 있는 사람수 계산
        count = stages.count(i)

        #실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length

        #리스트에 원소 삽입
        answer.append((i, fail))
        length -= count

    print(answer)
    answer = sorted(answer, key = lambda t:t[1], reverse=True)

    answer = [i[0] for i in answer]
    return answer


stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(5,stages)