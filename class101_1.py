def solution(N):
    enable = N % 10
    print("enable", enable)
    while N > 0:
        if enable == 0 and N % 10 != 0:
            enable = 1
        elif enable == 1:
            print(N % 10, end ='')
        N = N // 10

N = 10011
solution(N)