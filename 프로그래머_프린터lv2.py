def solution(priorities, location):

    answer = 0

    check = [0 for _ in range(len(priorities))]
    check[location] = 1

    while True:
        if priorities[0] == max(priorities):
            answer += 1

            if check[0] != 1:
                del priorities[0]
                del check[0]
            else:
                return answer
        else:
            priorities.append(priorities[0])
            check.append(check[0])
            del priorities[0]
            del check[0]

priorities = [2, 1, 3, 2]
priorities1 = [1, 1, 9, 1, 1, 1]
location = 2
location1 = 5

solution(priorities, location)