import math

N = int(input())

ans = []
check = []
for i in range(9999667):
    reple = str(i)
    if reple.count("6") >= 3:
        # check.append(str(i))
        flag = 0
        for p1, p2, p3 in zip(reple, reple[1:], reple[2:]):
            if p1 == p2 == p3 == "6":
                check.append(int(i))
                break
    if (len(check)>=N):
        print(check[len(check)-1])
        break

# N번째 작은 숫자임으로 for문 증가시키면서 하나씩 돌리고, 문자열 비교를 통해서 연속 3자리가 6이면 체크 베열에 더하고
# 그 배열은 작은것부터 들어감으로 순서에 상관없으며, 맨 마지막 배열의 원소를 출력 