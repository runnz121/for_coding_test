def solution(arr):
    answer = 0
    check = [False] * len(arr)

    dict_arr=[]
    for i in range(len(arr)):
        db = dict()
        elements = list(str(arr[i]))
        for ele in elements:
            if ele not in db:
                db[ele] = 1
            else:
                db[ele] += 1
        #answer += 1
        #print(check)
        # 위에서 만든 dict를 갖고 비교를 시작
        dict_arr.append(db)
    #print("std", dict_arr)

    for i in range(len(arr)):
        if not check[i]:
            check[i] = True
            answer += 1
            for j in range(i, len(arr)):
                if dict_arr[i] == dict_arr[j]:
                    check[j] = True
    #print(answer)
    return answer

arr = [112, 1814, 121, 1481, 1184]
solution(arr)