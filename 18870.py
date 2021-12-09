import sys
T = int(input())
arr = list(map(int, sys.stdin.readline().split()))
ans = []

db = dict()
arr1 = list(set(arr))
arr1.sort()
#print(arr1)
# 정렬된 원소의 인덱스 = 원본 배열에 해당 원소가 몇번재 인덱스에 있는가
for i in range(len(arr1)):
    db[arr1[i]] = i # dict 은 시간 복잡도가 O(N(1)) 임으로 딕셔너리로 해야 시간초과 안뜸

for x in range(len(arr)):
   print(db.get(arr[x]), end =' ')
