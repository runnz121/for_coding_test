n = int(input())
strings = str(input())

sums = 0
for i in range(n):
    k = ord(strings[i]) - 96
    sums += k * 31**(i)

print(sums%1234567891)