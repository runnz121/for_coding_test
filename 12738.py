# lower bound 이용
# 이분탐색을 이용해서 오름차순으로 정렬된 배열에서 처음으로 특정값 이상이 나오는 인덱스를 반환

import sys

input = sys.stdin.readline

def binary(start, end, num):
    while start < end:
        mid = (start + end) // 2
        if answer[mid] < num:
            start = mid + 1
        else:
            end = mid
    return end

n = int(input())
arr = list(map(int, input().split()))

answer = []
for num in arr:
    if len(answer) == 0:
        answer.append(num)
        continue

    # 정답 배열에서 마지막 값이 현재 배열값보다 작은 경우 -> 정답 배열에 추가(증가 수열로 저장)
    if answer[-1] < num:
        answer.append(num)
    else:
    # 그렇지 않다면 이분탐색을 통해 현재 값이 들어갈 배열을 업데이트 해줌 -> nlogn으로 돌림, 무조건 1회에 통과해줘야 함으로 logN의 의 이진탐색을 통해 업데이트를 해주는 식으로 구현됨
        idx = binary(0, len(answer) - 1, num)
        answer[idx] = num

print(len(answer))