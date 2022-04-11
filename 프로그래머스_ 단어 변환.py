

def solution(begin, target, words):
    answer = []
    check = []

    if target not in words:
        answer = 0
        return answer

    def dfs(start, depth, check):

        nonlocal answer

        if start == target:
            answer.append(depth)
            return

        for i in words:
            dif = 0
            if i not in check:
                for idx in range(len(i)):
                    if i[idx] != start[idx]:
                        dif += 1
                if dif == 1 and i in words:
                    check.append(i)
                    dfs(i, depth + 1, check)
                    check.pop()

    dfs(begin, 0, check)
    #print(answer)

    if len(answer) == 0:
        answer = 0
    else:
        answer = min(answer)
    print(answer)
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin, target, words)
