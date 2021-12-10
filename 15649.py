import sys
a, b, = map(int, input().split())
arr = [] # 정답 누적
def back(depth):
    if depth == b: #해당 for문 종료조건(for 문 몇번 반복할건지)
       # print(arr)
        print(' '.join(map(str, arr)))
        return
    for j in range(1, a+1):
        if j not in arr:
            arr.append(j) # 체크배열에 해당 값을 담는다
            back(depth + 1) # 깊이를 하나 더 증가시킴
            #print("2", arr)
            arr.pop() #해당 배열에서 원소값을 빼줌으로서 호출되기전 함수로 돌아가게 한다(함수 재사용)//pop은 맨 마지막 요소를 뺌
            #print("3", arr)
back(0)


# for i in range(1, a+1):
#     for j in range(1, a+1-1):
#         print(f'{i} {j}')