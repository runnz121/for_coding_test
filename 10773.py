from collections import deque

deq = deque()

T = int(input())

for _ in range(T):
    number = int(input())
    if number == 0:
        deq.pop()
    else:
        deq.append(number)

print(sum(deq))