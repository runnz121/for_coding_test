n = int(input())
arr = list(map(int, input().split()))

lens = len(arr)

def gcd(a, b):
    while b > 0:
        a, b, = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)


k = 1
if lens >= 2:
    k = lcm(arr[0], arr[1])
else:
    print(arr[0])
    exit()

idx = 1
while idx < lens-1:
    k = lcm(k, arr[idx + 1])

    idx += 1

print(int(k))