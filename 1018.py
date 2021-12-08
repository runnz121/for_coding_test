import sys,math
y, x = map(int, input().split())

arr = []
for i in range(y):
    arr.append(sys.stdin.readline()[:-1])
count = 0
min_value = 1e9
for i in range(y+1-8):
    #print("i",i)
    for j in range(i, i+8):
        print(arr[j] ,"end1")
        for a in range(x+1-8):
            str = arr[j][a:a+8]
            print(str)
            for p1, p2 in zip(str,str[1:]): #스트링 한줄 비교
                if p1 == p2:
                    count +=1
        count -= 2
        count /= 2
       # print("ct",str)
        min_value = min(count, min_value)
        count = 0
print(math.ceil(min_value))




        # for a in range(x+1-8):
        #     print(arr[j][a])
        #     for b in range(a+1, a+8):
        #        # print(arr[j][b])
        #         if arr[j][b-1] == arr[j][b]:
        #             #print(arr[j][b])
        #             count += 1
        #             #print("count",count)
    # count /= 2
    # min_value = min(count, min_value)
    # count = 0
    # print(math.ceil(min_value))
    # print("end")
