import math

T = int(input())

while T > 0 :
    N = int(input())
    minCheck = []

    #에라토스테네스의 체
    arr = [True for i in range(N+1)]
    for i in range(2, int(math.sqrt(N))+1):
        if arr[i] == True:
            j = 2
            while i * j <= N:
                arr[i * j] = False
                j +=1

    #소수만 있는 배열에서 들어온수 빼기 소수해서 해당 소수가 존재시 체크배열에 넣음
    for j in range(2, len(arr)):
        if arr[j] == True:
            if arr[N-j] == True:
                minCheck.append((j, N-j))
    min_value = 1e9
    ans =""
    #작은순서대로 나오게 하기위해 정렬
    minCheck.sort(key = lambda x : x[1])
    for k in range(len(minCheck)):
      #절대값 기준으로 변경
        if abs(minCheck[k][1]-minCheck[k][0]) < min_value:
            min_value = abs(minCheck[k][1]-minCheck[k][0])
            ans = str(minCheck[k][1])+" "+str(minCheck[k][0])
    print(ans)
    T -=1

