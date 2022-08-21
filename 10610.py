n = input()
arr = list(map(int,n))
b = sum(arr)


# 30의 배수가 되는 조건
#
# - 일의 자리수가 0이여야 함.
#
# - 각 자리의 숫자들을 더했을때 3으로 나누어 떨어져야함.
if b%3==0:
    arr.sort(reverse=True)
    c = arr[-1]

    if c==0:
        a = ''.join(map(str,arr))
        a = int(a)
        print(a)
    else:
        print(-1)

else:
    print(-1)