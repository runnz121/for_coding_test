T = int(input())
arr = list(map(int, input().split()))

def get_gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

gcd = arr[0]
for i in arr[1:]:
    ggg = get_gcd(gcd, i)
    first = gcd // ggg
    second = i // ggg
    print(f'{first}/{second}')