n = int(input())
test = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0

for i in range(n):
    student = test[i]
    if student >= b:
        if (student - b) % c > 0:
            answer += (student - b) // c + 2
        # print(i)
        else:
            answer += (student - b) // c + 1
    elif student  < b and student >= c:
        if student % c > 0:
            answer += student // c + 1
        else:
            answer += student // c

print(answer)
