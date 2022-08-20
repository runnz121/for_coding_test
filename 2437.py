n = int(input())

arr = list(map(int, input().split()))

arr.sort()

flag = True

sums = 1

# 현재 뽑은 숫자가 누적합보다 크면 최소 값은 누적합 + 1
# 즉 현재 누적합 보다 현재 뽑은 숫자가 작으면 해당 숫자를 더한 범위 만큼의 수를 모두 만들 수 있다.
for i in arr:
    if sums < i:
        break
    sums += i

print(sums)