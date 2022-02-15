from itertools import permutations

def solution(numbers):
    answer = 0
    nums = []
    comb = []
    arr = []


    for i in numbers:
        nums.append(int(i))

    for i in range(1, len(nums)+1):
        comb.append(list(permutations(nums, i)))


    for i in comb:
        for j in i:
            res =''
            for k in range(len(j)):
                res += str(j[k])
                if int(res) not in arr:
                    arr.append(int(res))
    arr.sort()
    odd = ari(arr[-1]+1)
    for i in arr:
        if i in odd:
            answer += 1
    return answer

def ari(n):

    siv = [True] * n
    res = int(n**0.5)
    for i in range(2, res + 1):
        if siv[i] == True:
            for j in range(i+i, n, i):
                siv[j] = False
    return [i for i in range(2, n) if siv[i] == True]


numbers = "17"
solution(numbers)