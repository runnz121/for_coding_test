n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))

    idx = arr[0]
    student = arr[1:]

    student.sort(reverse=True)

    maxGap = 0
    for k in range(idx-1):
        maxGap = max(maxGap, student[k] - student[k + 1])

    student.sort()

    print("Class " + str(i + 1))
    print("Max " + str(student[idx-1]) + ", Min " + str(student[0]) + ", Largest gap " + str(maxGap))
