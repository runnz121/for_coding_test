
n = int(input())

a, b = 0, 1
answer = []

if n == 1:
    answer.append(0)
    answer.append(1)
else:
    arrB = [0 for i in range(n)]
    arrB[0] = 1
    arrB[1] = 1

    for i in range(2, n):
        k = arrB[i-1] + arrB[i-2]
        arrB[i] = k

    answer.append(arrB[n-2])
    answer.append(arrB[n-1])

print(*answer)


# 1
# 0 1

# 2
# 1 1

# 3
# 1 2

# 4
# 2 3

# 5
# 3 5

# 6
# 5 8

# 7
# 8 13

# 8
# 13 21

# 9
# 21 34

# 10
# 34 55