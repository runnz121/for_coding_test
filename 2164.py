from collections import deque

T = int(input())

arr = deque()
for i in range(1,T+1):
    arr.append(i)

while len(arr) != 1:
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])