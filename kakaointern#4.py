from itertools import combinations

def solution(arr, m):
    arr1 = list(combinations(arr, m)) # 조합
    #print(sorted(arr1))

    globalmax = 0
    for i in range(len(arr1)):
        res = list(combinations(arr1[i], 2)) # [(4, 3), (4, 2), (3, 2)]
        #print(res)
        submin = 1e9
        for j in range(len(res)):
            sub = res[j][0] - res[j][1]
            if sub < 0:
                sub = sub *(-1)
            #print(sub, res)
            submin = min(submin, sub)
        globalmax = max(submin, globalmax)

    return(globalmax)
    #print(globalmax)



arr = [1,2,4,5,8]
m = 3
solution(arr,m)