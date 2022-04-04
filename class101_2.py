def solution(N):
    enable = N % 10
    print("enable", enable)
    print("N", N)
    while N > 0:
        if enable == 0 and N % 10 != 0:
            enable = 1
        if enable == 1:
            print(N % 10, end ='')
        N = N // 10

N = 123450
solution(N)