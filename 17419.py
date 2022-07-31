import sys

input = sys.stdin.readline

n = int(input())
s = str(input())
cnt = 0
for i in s:
    if i == '1':
        cnt += 1
print(cnt)
#
# s = bin(int('0b' + str(s),2))
# print(s)
# s = bin(int(s,2))
# print(s)