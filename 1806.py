import sys
input = sys.stdin.readline
a, b = map(int, input().split())
arr=list(map(int, input().split()))

lens = sys.maxsize

start = 0
end = 1

while start < a:
    res = 0
    for i in range(start, end-start):
        res += arr[i]

    print(res)
    if res >= b:
        lens = min(lens, end-start+1)

        start += 1
        end = start + 1
    else:
        end += 1
    if end > a:
        start += 1
        end = start + 1
    if lens == 2:
        break

if lens == sys.maxsize:
    print(0)
else:
    print(lens)