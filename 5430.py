from collections import deque
import sys

que = deque()

T = int(input())

while T > 0:
    # 함수 받기
    fun = list(str(sys.stdin.readline()[:-1]))
    # 배열 갯수
    lens = int(input())
    # 배열
    strs = str(sys.stdin.readline()[:-1])
    strs = strs[1:-1]
    arr_strs = strs.split(',') # ['1', '1', '2', '3', '5', '8']
    arr_int = deque()


    for i in arr_strs:
        if i == '':
            arr_int = []
        else:
            arr_int.append(int(i))

    ans = '['
    #함수의 길이는 테스트케이스보다 작거나 같아야만 한다


    flag = 0
    cnt = 0
    # 출력하는 함수 D만을 카운트해서 에러처리해야함
    if fun.count('D') <= lens:
        # print('1')

        #시간초가 때문에, flag 를 세워서 reverse 한 것 처럼 구현함

        for i in fun:
            if i == 'R':
                if flag == 0:
                    flag = 1
                elif flag == 1:
                    flag = 0
                    cnt = 0
                #arr_int[len(arr_int)-1], arr_int[0] = arr_int[0], arr_int[len(arr_int)-1]
                #arr_int.appendleft(arr_int.pop())
                #arr_int.reverse()
            elif i == 'D':
                #reverse해서 출력 할 경우:
                if flag == 1:
                    arr_int.pop()
                # 정상 출력할 경우:
                else:
                    arr_int.popleft()
        if len(arr_int) == 0:
            ans += ']'
        else:
            # 마지막에 reverse해서 출력할 경우 배열 뒤집기
            if flag == 1:
                arr_int.reverse()
            while len(arr_int) != 0:

                res = arr_int.popleft()
                if len(arr_int) != 0:
                    ans += str(res) + ','
                else:
                    ans += str(res) + ']'
        sys.stdout.write(ans+'\n')
    elif lens == 0:
        # print('2')
        for i in fun:
            if i == 'R':
                ans += ']'
            elif i == 'D':
                ans = 'error'
        sys.stdout.write(ans+'\n')
    else:
        # print('3')
        sys.stdout.write('error\n')
    T -=1