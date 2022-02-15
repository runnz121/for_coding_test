def solution(N, number):

    # 숫자 사용 횟수를 dp로 만듬
    arr = [None] + [{int(str(N) * i)} for i in range(1, 9)]

   # print(arr) :  [None, {2}, {22}, {222}, {2222}, {22222}, {222222}, {2222222}, {22222222}]

    for i in range(1, 9): # 총 8번 돌음
        for j in range(1, i): # 숫자 사용 횟수
            for num1 in arr[j]: #  2가 2번 사용 되었을 경우 (22) num1 = 22 -> i = 3, j = 1, 2 -> 3번
                for num2 in arr[i - j]: #
                    print(arr[i], arr[j], num1, num2, i, j)
                   # 즉 해당 숫자를 사용해서 만들어진 수를 그 배열에 넣겠다는 뜻
                    arr[i].add(num1 + num2)
                    arr[i].add(num1 - num2)
                    arr[i].add(num1 * num2)
                    if num2:
                        arr[i].add(num1 // num2)

                        # 예를 들어서 3개를 갖고 만드는 경우 i = 3 이되고, 이것은
                        # i = 1, i = 2 를 갖고 만드는 경우를 따지면되고
                        # 이것을 해당  i 번째의 배열에 추가해준다( 뒤에 갈 수록 그것으로 만든 숫자들을 다시 재사용 할것이기 때문)


        if number in arr[i]:
            print(i)
            return i


    return -1

N = 2
number = 11
solution(N, number)
