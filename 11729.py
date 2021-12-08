#하노이 탑 규칙
# 이동하려는 원판의 수가 홀수일때 -> 목표 막대로 보냄
# 이동하려는 원판의 수가 짝수일때 -> 목표 제외로 보냄

# https://study-all-night.tistory.com/6
# https://data-jj.tistory.com/34

# 1단계 n-1개의 원판을 1번 막대에서 2번막대로 옮김(나머지 막대기에 옮김)
# 2단계 남은 1개의 원판을 1번 막대에서 3번 막대로 옮김(목적지 막대기에 옮김)
# 3단계 n-1개의 원판을 2번 막대에서 3번 막대로 옮김

#6-start-end : 전체 막대의 합은 (1+2+3으로 6 따라서 처음 막대와 나중막대 값을 빼주면 나머지막대의 값을 알 수 있다)
#start막대에서 end막대로 옮겨주면 됨

#1안

# def hanoi(n, start, end):
#     if n == 1:
#         print(start, end)
#         return
#     hanoi(n-1, start, 6-start-end) # 1단계
#     print(start, end) # 2단계
#     hanoi(n-1, 6-start-end, end) # 3단계
#
# n = int(input())
# print(2**n-1)
# hanoi(n, 1, 3) # 무조건 처음 이동하는 순서

#2안

def hanoi(n, a, b):
    if n > 1:    #start,end
        hanoi(n-1, a, 6-a-b)  # 기둥이 1개 이상이면 그룹으로 묶인 n-1개 원판을
                              # 중간으로 먼저 다 옮긴다
    print(a, b)

    if n > 1:
        hanoi(n-1, 6-a-b, b)
n = int(input())

print(2**n -1)                # 총 이동해야 하는 횟수
hanoi(n, 1, 3)

