from collections import deque


def solution(begin, target, words):
    answer = 0

    arr = []

    if target not in words:
        return answer

    for word in words:
        for k in word:
            arr.append(k)

    sets = list(set(arr))

    cc = [False] * len(words)

    def dfs(begin, depth):

        if depth > len(words):
            return depth

        for i in range(len(sets)):
            for j in range(len(begin)):
                re = begin[:j] + sets[i] + begin[j + 1:]
                if re == target:
                    return depth

                elif re in words:
                    cc[words.index(re)] = True
                    dfs(re, depth + 1)

    answer = min(dfs(begin, 0), answer)

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin, target, words)
