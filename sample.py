from collections import deque

db = deque()

db.append([1,1])
db.append([2,2])

if [1,2] in db:
    print('yes')