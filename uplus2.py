import copy


def solution(compressed):

    comp = list(compressed)

    answer = recurse(comp)

    print(answer)
    return answer


def recurse(comp):
    flag = False

    for i in range(len(comp)):
        if comp[i].isnumeric():
            flag = True

    for i in range(len(comp)):
        # 숫자인지 판별
        if comp[i].isnumeric():
            multi = int(comp[i])

            comp = comp[i + 2: -1]
            comp = ''.join(comp)

            return recurse(comp * multi)
    if flag == False:
        return comp

compressed = "2(3(hi)co)"
solution(compressed)