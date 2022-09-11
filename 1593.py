g, s = map(int, input().split())
W = input()
S = input()

answer = 0
wa = [0] * 58
sa = [0] * 58

for x in W:
    wa[ord(x) - 65] += 1


# 구간 비교를 시작할 시작점 start와 현재 카운팅한 알파벳 길이 length를 초기화하고 시작한다.
start, length = 0, 0


for i in range(s):
    sa[ord(S[i]) - 65] += 1
    length += 1

    # 길이가 서로 같아지는 순간
    if length == g:
        if wa == sa: # 두 배열의 문자값이 서로 같으면
            answer += 1 # 답 증가
        sa[ord(S[start]) - 65] -= 1  #슬라이딩 윈도우로 앞의 원소값의 해당하는 문자 갯수를 한개 빼줌
        start += 1 # 길이가 증가했음으로 다음 문자열로 증가 ['a' -> 'b']
        length -= 1 # 전체 길이 줄여줌

print(answer)