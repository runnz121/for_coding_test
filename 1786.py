
# c++
# https://bowbowbow.tistory.com/6

# python
# https://yiyj1030.tistory.com/495

# pi 배열값을 얻는다
def getPi(p):
    # 문자열 길이를 구함
    str_len = len(p)
    # 문자열 비교를 위해 첫번째 인덱스를 고정하기 위한 변수
    j = 0
    # pi 테이블을 문자열 길이만큼 0 으로 초기화 한다
    pi = [0] * str_len
    # 문자열 인덱스 1부터 for문 돌림
    for i in range(1, str_len):
        # 이 부분을 통해 한번에 건너뛴다 ->
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(s, p):
    res = []
    count = 0
    pi = getPi(p)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == (len(p) - 1):
                res.append(i - len(p) + 2)
                count += 1
                j = pi[j]
            else:
                j += 1
    print(count)
    for element in res:
        print(element)
T = input()
P = input()
kmp(T, P)


# def kmp1(s, p):
#     # 결과를 담을 배열
#     res = []
#     # 찾을 패턴 문자열 기준으로 pi 배열을 생성
#     pi = getPi(p)
#     # 비교 대상 문자열 길이
#     len_s = len(s)
#     # 기준 대상 문자열 길이
#     len_p = len(p)
#     j = 0
#     for i in range(len_s):
#         while j > 0 and s[i] != p[j]:
#             j = pi[j - 1]
#         if s[i] == p[j]:
#             if j == len_p - 1:
#                 res.append(i - len_p + 1)
#                 j = pi[j]
#             else:
#                 j += 1
#     return res

