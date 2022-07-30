from collections import deque

def solution(ing, st, tar):

    left = st
    right = st

    lcnt = 1
    rcnt = 1

    while True:
        if ing[left] == tar:
            break
        else:
            left -= 1
            lcnt += 1

            if left < 0:
                left = len(ing) -1

    while True:
        if ing[right] == tar:
            break
        else:
            right += 1
            rcnt += 1

            if right >= len(ing):
                right = 0


    return min(lcnt, rcnt)

ing = ['a','b','c','d']
st = 1
tar = 'd'
print(solution(ing, st, tar))