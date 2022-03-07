import sys
# https://backtony.github.io/algorithm/2021-02-18-algorithm-boj-class4-20/

# default 값이 1000이다
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def post_order(start, end):
    # 역전시 리턴
    if start > end:
        return

    # 루트 노드 -> start는 인덱스
    root = pre_order[start]
    idx = start + 1

    # root보다 커지는 지점을 찾는 과정
    # for문으로 찾으면 안된다. 아래서 설명
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    # 왼쪽 서브트리
    post_order(start + 1, idx - 1)

    # 오른쪽 서브트리
    post_order(idx, end)

    # 후위순회이므로 제일 마지막에 찍으면 된다
    print(root)


pre_order = []
while 1:
    try:
        pre_order.append(int(input()))
    # try에서 예외 발생시 break 실행 -> 계속 입력받다가 공백이 들어오면 에러 발생 입력받는 while문 종료
    except:
        break

# 배열 길이보다 하나 짧은것 부터 시작함
post_order(0, len(pre_order) - 1)