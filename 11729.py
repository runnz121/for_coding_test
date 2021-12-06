#하노이 탑 규칙
# 이동하려는 원판의 수가 홀수일때 -> 목표 막대로 보냄
# 이동하려는 원판의 수가 짝수일때 -> 목표 제외로 보냄

from collections import deque

n = int(input())
que1 = deque()
que2 = deque()
que3 = deque()


plates = dict()
for i in range(1, n+1):
    que1.append(i)

total = 0
def Hanoi(leftplates, total):
    if leftplates == 0:
        que1.appendleft(que2.popleft())
        total +=1
        return Hanoi(len(que1),total)
    #남은판의 갯수가 짝수개면 -> 2번플레이트
    if leftplates % 2 == 0:
        que1pop = que1.popleft()
        if que1pop < que2.popleft():
            que2.appendleft(que1pop)
            froms = 1
            to = 2
            total += 1
            print(f'{froms} {to}')
            return Hanoi(len(que1), total)
    #남은판의 갯수가 홀수이면 -> 3번플레이트(목표)
    else:
        que1pop = que1.popleft()
        if que1pop < que3.popleft():
            que3.appendleft(que1pop)
            to = 3
            froms = 1
            total += 1
            print(f'{froms} {to}')
            return Hanoi(len(que1), total)
        else:
            que2.appendleft(que3.popleft())
            total += 1
            return Hanoi(len(que2), total)
print(Hanoi(n))