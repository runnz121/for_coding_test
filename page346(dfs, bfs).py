# 균형잡힌 괄호 문자열(갯수가 맞는지만 확인)
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


# 올바른 괄호문자열(갯수도 맞고 열고 닫음이 확실함)
def check_proper(p):
    count = 0 #왼쪽 괄호 갯수 만
    for i in p:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False #쌍이 맞지 않으면 False
            count -= 1
    return True #쌍이 맞으면 true

def solution(p):
    answer = ""
    if p == "":
        return answer
    index = balanced_index(p)
    u = p[:index + 1] #처음부터 index + 1까지
    v = p[index + 1:] #index + 1 부터 끝까지

    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])  # 첫번째와 마지막 문자 제거 -> 처음과 마지막문자만 뺴고 리스트로 반환
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
