def solution(s):
    answer = []
    cnt = 0
    flag = 0

    s_len = len(s)

    # start = s[0]
    # end = s[len(s)-1]


    #처음과 끝이 같으면,
    # if start == end:
    #     s2 = s + s
    # else:
    #     s2 = s
    s2 = s + s

    for i in range(0, len(s2) - 1):
        #print(s2[i])
        if i >= s_len and flag == 1:
            break
        else:
            if s2[i] == s2[i+1]:
                cnt += 1
            else:
                if i >= s_len:
                    flag = 1
                cnt += 1
                answer.append(cnt)
                cnt = 0
    answer = answer[1:]
    answer.sort()
    #print(answer)

    return answer

s = "aaabbaaa" # 3 2 3 6 -> 2 6
s1 = "wowwow" # 1 1 2 1 2 -> 1212
s2 = "aaabbaaaxa" # 3 2 3 1 4 -> 2 3 1 4 -> 1 2 3 4
s5 = "asdfa" # 1 1 1 1 2
print(solution(s5))

#맨앞 뒤 같으면 맨 처음 샌거 없엔다,
# 1 2 1 2

#
# 문제 설명
# 처음과 끝이 이어져 있는 문자열을 상상해봅시다. 당신은 해당 문자열 내의 "같은 글자가 연속해 있는" 구간들을 추출하고자 합니다.
#
# 문자열 s가 매개변수로 주어집니다. s 내의 모든 "같은 글자가 연속해 있는" 구간의 길이를 각각 배열에 담아 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 3 ≤ s의 길이 ≤ 1,000
# s는 영어 소문자로 이루어진 문자열입니다.
# 입출력 예
# s	result
# "aaabbaaa"	[2,6]
# "wowwow"	[1,1,2,2]
# 입출력 예 설명
# 입출력 예 #1
#
# 다음 애니메이션은 처음과 끝이 이어진 "aaabbaaa"의 각 구간을 구하는 과정을 나타낸 것입니다.
# ex1
#
# 각 구간의 길이는 6("aaaaaa"), 2("bb")이므로, 이를 정렬한 [2,6]을 return 해야 합니다.
# 입출력 예 #2
#
# 다음 애니메이션은 처음과 끝이 이어진 "wowwow"의 각 구간을 구하는 과정을 나타낸 것입니다.
# ex2
#
# 각 구간의 길이는 2("ww"), 1("o"), 2("ww"), 1("o")이므로, 이를 정렬한 [1,1,2,2]를 return 해야 합니다.