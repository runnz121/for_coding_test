def solution(arr):
    answer = 0


    for i in range(len(arr)):
        ans = [arr[i]]
        for j in range(i+1, len(arr)):
            if arr[j] in ans:
                flag = True
            else:
                flag = False

            if j % 2 == 0:
                if flag:
                    ans.append(arr[j])
                else:
                    print(ans)
                    break
            else:
                ans.append(arr[j])

    print(answer)
    return answer

arr = [5, 2, 3, 3, 5, 3]
solution(arr)


#다음과 같은 조건을 모두 만족하는 수열 x를 스타 수열이라고 정의합니다.

# x의 길이가 2 이상의 짝수입니다. (빈 수열은 허용되지 않습니다.)
# x의 길이를 2n이라 할 때, 다음과 같은 n개의 집합 {x[0], x[1]}, {x[2], x[3]}, ..., {x[2n-2], x[2n-1]} 의 교집합의 원소의 개수가 1 이상입니다.
# x[0] != x[1], x[2] != x[3], ..., x[2n-2] != x[2n-1] 입니다.
# 예를 들어, [1,2,1,3,4,1,1,3]은 스타 수열입니다. {1,2}, {1,3}, {4,1}, {1,3} 의 교집합은 {1} 이고, 각 집합 내의 숫자들이 서로 다르기 때문입니다.
# 1차원 정수 배열 a가 매개변수로 주어집니다. a의 모든 부분 수열 중에서 가장 길이가 긴 스타 수열의 길이를 return 하도록 solution 함수를 완성해주세요. 이때, a의 모든 부분
#
# console.log(solution([0]) == 0)
# console.log(solution([5, 2, 3, 3, 5, 3]) == 4)
# console.log(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]) == 8)