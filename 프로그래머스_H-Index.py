def solution(citations):
    citations = sorted(citations, reverse=True)
    check = []
    #0이 아니고 다음 인덱스 기준으로 학인
    for i in range(len(citations)):
        if citations[i] >= len(citations[:i]) and citations[i] !=0:
            check.append(citations[i])
    answer = len(check)
    #print(answer)
    return answer


citations = [3, 0, 6, 1, 5]
t1 = [0,1,2]
# solution(citations)
solution(t1)