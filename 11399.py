T = int(input())

# arr[i] -> i번째 있는 사람이 돈을 뽑는데 걸리는 시간
arr = list(map(int, input().split()))

arr.sort()

susms = []
for i in range(T+1):
    sums = 0
    for j in range(0,i):
        sums += arr[j]
    susms.append(sums)
print(sum(susms))