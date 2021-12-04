def solution(stockPrices, k):
    min_value = 0
    length = 0
    ans = 0

    #3개씩 자르는 코드
    for i in range(len(stockPrices)-k+1):
        arr = stockPrices[i:i+k]
        print(arr)

        for j in arr:
            if min_value < j:
                min_value = j
                length +=1


        if length == k:
            ans += 1

        length = 0
        min_value = 0
    print(ans)


stockPrices = [7,1,2,3,6,9,12,3]
k = 2
solution(stockPrices,k)