n = int(input())

# 1, 3, 4, 9, 10, 12

x = bin(n)

binx = x[2:]

binx = list(binx)

# n을 2진수로 바꿈
# 이 바꾼 2진수를 3진수로 바꿈
answer = 0
for i in range(len(binx)):
    if int(binx[i]) == 1:
        answer += 3 ** (len(binx)-i-1)

print(answer)