# import sys
#
# T = int(input())
# arr = [0] * 10001
#
# for _ in range(T):
#     arr[int(sys.stdin.readline())] += 1
#
# for j in range(10001):
#     if arr[j] != 0:
#         for i in range(arr[j]):
#             print(i)

import sys
n = int(sys.stdin.readline())
check = [0] * 10001 #메모리 초과 때문에 애초에 배열로 미리 메모리 할당

for _ in range(n):
    # num = int(sys.stdin.readline())
    # # 같은 수가 여러번 입력될 수 있음으로 해당 수가 들어오면 + 1로 처리함
    # check[num] = check[num] + 1

    check[int(sys.stdin.readline())] +=1

# print(check)

for i in range(10001):
    if check[i] != 0: # 체크 배열이 0이 아니면(수가 해당 인덱스에 존재하는 경우)
        for j in range(check[i]): # 입력된 갯수만큼 반복 출력
            sys.stdout.write(str(i)+'\n') # stdout으로 출력해야 메모리초과 안남 ㅡㅡ
