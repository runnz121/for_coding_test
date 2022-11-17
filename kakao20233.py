import copy

cases = []

def solution(users, emoticons):
    answer = []

    edr = [10,20,30,40]
    tmp = []
    check = [False] * len(emoticons)

    # 모든 케이스 추출
    #back(0, check, edr, tmp)

    allCase = []
    for i in emoticons:
        tmp = []
        for j in edr:
            tmp.append([i, j])
        allCase.append(tmp)

    for k in allCase:
        print(k)

    empty = []
    back(0, check, empty)

    for i in cases:
        print(i)


    for idx in range(len(allCase)):
        for i in cases:
            for j in i:
                print(allCase[idx][j])
    #print(allCase)




    return answer

def back(depth, check, tmp):

    global cases

    tmp1 = copy.deepcopy(tmp)

    if depth == len(emoticons):
        cases.append(tmp1)
        return

    for i in range(len(emoticons)):
        if check[i]:
            continue
        tmp.append(i)
        #check[i] = True
        back(depth + 1, check, tmp)
        tmp.pop()
        #check[i] = False



# def back(depth, check, edr, tmp):
#
#     global cases
#
#     tmp1 = copy.deepcopy(tmp)
#
#     if depth == len(emoticons):
#         cases.append(tmp1)
#         return
#
#     for i in range(len(emoticons)):
#         if check[i]:
#             continue
#         tmp.append([emoticons[i], edr[i]])
#         check[i] = True
#         back(depth + 1, check, edr, tmp)
#         tmp.pop()
#         check[i] = False






users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
solution(users, emoticons)