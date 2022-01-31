import sys
x = str(sys.stdin.readline().rstrip())
#
# db = [] * 100001
#
# for i in range(len(x)):
#     db.append([i,x[:i]])
#
#
# res = sorted(db, key = lambda x:x[1])

for i in range(len(x)):
    print(i)