import math

def solution(progresses, speeds):
    answer = []
    days = [0] * 101
    db = dict()

    # min_value = (100-progresses[0])//speeds[0]
    # print(min_value)
    min_value = 0
    # days[min_value] = 1
    for i in range(len(progresses)):
        res = 100- progresses[i]
        if res % speeds[i] > 0:
            day = res//speeds[i] + 1
        else:
            day = res//speeds[i]
        #print(progresses[i], day)
        # day = math.ceil(res//float(speeds[i]))+1
        # print(min_value, day, days)
        if day <= min_value:
            days[min_value] += 1
        else:
            days[day] +=1
            min_value = day

    for i in days:
        if i != 0:
            answer.append(i)
    #print(answer)
    return answer

progresses = [5,5,5]
progresses1 = [95, 90, 99, 99, 80, 99]

speeds = [21,25,20]
speeds1 = [1, 1, 1, 1, 1, 1]
solution(progresses, speeds)