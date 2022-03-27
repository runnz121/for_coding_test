from collections import deque

def solution(s):

    answer = ''

    db = {"1" : [".","Q","Z"], "2" :["A","B","C"], "3" : ["D","E","F"],"4": ["G","H","I"], "5" : ["J","K","L"],
          "6": ["M","N","O"], "7" : ["P","R","S"], "8" :["T","U","V"], "9" : ["W","X","Y"] ,"0": [""]}

    check = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0 , "0" : 0}


    q = deque(s)


    cache = q.popleft()
    check[cache] += 1
    while q:
        x = q.popleft()

        if x == "0":
            answer += db[cache][check[cache] - 1]
            check[cache] = 0
            cache = x
            continue

        if x == cache:
            check[x] += 1
        else:
            answer += db[cache][check[cache] -1]
            check[cache] = 0

            cache = x
            check[x] += 1

    for key in check.keys():
        if check[key] != 0:
            answer += db[key][check[key] - 1]


    return answer

s = "2220281"
solution(s)