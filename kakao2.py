from collections import deque

def solution(s):
    b = '0' * len(s)
    b = bin(int(b, 2))

    for i in range(len(s)+1):
        b = bin(int(b, 2) | (1 << i))
        b = bin(~int(b, 2))

    return bin(int(b,2))

strs = '1100'
print(solution(strs))


