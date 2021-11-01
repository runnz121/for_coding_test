array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array) + 1) #리스트의 최대값에 1을 더한 빈 리스트를 선언

for i in range(len(array)):
    count[array[i]] += 1 #각 데이터의 해당하는 인덱스값 증가

print(count)

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')