def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]


    for i in range(len(requests)):
        flag = False
        if sticky == False:
            answer[i % servers].append(requests[i])
        else:
            for k in range(servers):
                if requests[i] in answer[k]:
                    answer[k].append(requests[i])
                    flag = True
                    break
            if flag == False:
                answer[i % servers].append(requests[i])
    return answer

print(solution(2, True, [1,2,2,3,4,1]))