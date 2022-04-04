def solution(S):
    ans = 0
    total = len(S)
    k = 0
    while k < total:
        if S[k] == 'X':
            ans += 1
            k += 3
        else:
            k += 1

    print(ans)
    return ans

S = "..XXX.XX"
solution(S)