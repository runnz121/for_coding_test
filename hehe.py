from collections import deque


que = deque()

que.append([1,2])
que.append([2,2])
que.append([3,4])
que.append([5,2])

print(que[0][0])
print(que)

if [1,2] in que:
    print('yes')
else:
    print("no")

# incheck 0 7
# deque([[1, 7], [2, 7]])
# deque([[1, 2], [2, 2], [3, 4], [5, 2]])