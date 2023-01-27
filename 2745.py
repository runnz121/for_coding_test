b, n = map(str, input().split())
b = ''.join(reversed(b))
nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lists_nums = list(nums)

n = int(n)


lens = len(b)


res = 0
for i in range(lens-1, -1, -1):
    find_n = lists_nums.index(b[i])
    sums = (n ** i) * find_n
    res += sums

print(res)