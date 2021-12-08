# https://cotak.tistory.com/38

def appendStar(len):
    if len == 1:
        return['*']

    Stars = appendStar(len//3)
    L = []

    # 빈배열에 재귀를 통해 구해진 별을 더함
    for S in Stars:
        L.append(S*3) # ***출력
    for S in Stars:
        L.append(S+' '*(len//3) + S) # * 3의 갯수만큼 공백 * 출력
    for S in Stars:
        L.append(S*3) # ***출력
    return L #위의 출력 조건을 배열에 담아 반환

n = int(input())
print('\n'.join(appendStar(n)))