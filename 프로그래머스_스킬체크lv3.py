def solution(A, B):
    answer = 0
    # A와 B를 정렬한다.
    A = sorted(A)
    B = sorted(B)
    print(A,B)

    for i in A:
        for j in B:
            # i와 j를 비교해서 j가 더 클경우 answer에 1을 더해주고 j는 이미 사용했으므로 j를 remove해준다.
            if i < j:
                print(i,j)
                answer += 1
                B.remove(j) # 다음 숫자 비교시 이미 사용한 숫자와 또 비교함으로 삭제 해줘야함
                break
    return answer

A = [5,1,3,7]
B = [2,2,6,8]
solution(A,B)