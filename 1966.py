testCase = int(input())

for _ in range(testCase):
    #문서 갯수, 중요도
    N, M = map(int,input().split())

    #문서 나열
    printList = list(map(int,input().split()))
    checkList = [0 for _ in range(N)] 
    checkList[M] = 1 # 궁금한 문서위치 저장

    count=0
    #첫번째값만 비교하면 됨!!!!!!!!!!1
    while True:
        #문서리스트의 첫번째값이 가장 큰 경우
        if printList[0] == max(printList):
            count+=1 # 1 더해줌

            #체크 리스트에 첫번째가 0이 아니면, 문서리스트에서 1, 체크리스트에서 1 삭제
            if checkList[0] != 1:
                del printList[0]
                del checkList[0]
            else:
                print(count) # 바로 출력
                break
        # 첫번째값이 타겟값이 아니 라면 계속 반복 돌림
        else:
            printList.append(printList[0])
            checkList.append(checkList[0])
            del printList[0]
            del checkList[0]
