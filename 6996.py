n = int(input())

for _ in range(n):
    x, y = map(str, input().split())

    x1 = list(x)
    y1 = list(y)


    x1.sort()
    y1.sort()
    flag = True

    if len(x1) != len(y1):
        print(x, "&", y, "are NOT anagrams.")
        flag = False

    for i in range(len(x1)):
        if flag == True and x1[i] != y1[i]:
            print(x, "&", y, "are NOT anagrams.")
            flag = False
            break

    if flag == True:
        print(x, "&", y, "are anagrams.")