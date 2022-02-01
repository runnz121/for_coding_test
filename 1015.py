n = int(input())
t = list(map(int, input().split()))

s_li = sorted(t)

# s_li 수열에서 가장 큰 값 == li 배열에서 가장


li = []

for i in range(n):
    # 처음 입력받은 배열 t에서 해당 원소를 갖고 있는 s_li배열에서(오름차순) 그 값의 인덱스를 새로운 배열에 추가함
    # 2 3 1 -> t 배열
    # 1 2 3 -> s_li배열g
    # t[0] = 2 이고 이 값은 s_li 배열에서 1번 인덱스에 있다
    # 이 인덱스 값을 li 배열에 추가해줌
    # 그리고 s_li배열에서 추가한 값 중복방지를 위해 -1로 처리해줌(-1은 t 배열에 없음으로)
    idx = s_li.index(t[i])
    li.append(idx)
    s_li[idx] = -1 # 수열값 변경으로 더이상 못넣게 함
print(*li)