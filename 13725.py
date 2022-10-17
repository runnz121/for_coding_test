import sys

input = sys.stdin.readline

x = str(input())

lens = len(x)

x = list(x)

p, r = -1

for i in range(lens):
    if i > r :
        p = r = i

        while r < lens and r <= 2*p and x[r] == x[2 * p - r]:
            r += 1

        res[i] = r -p