def solution(s):
    answer = 0

    if '999' in s:
        answer = 999
    elif '888' in s:
        answer = 888
    elif '777' in s:
        answer = 777
    elif '666' in s:
        answer = 666
    elif '555' in s:
        answer = 555
    elif '444' in s:
        answer = 444
    elif '333' in s:
        answer = 333
    elif '222' in s:
        answer = 222
    elif '111' in s:
        answer = 111
    elif '000' in s:
        answer = 0
    else:
        answer = -1
    return answer
