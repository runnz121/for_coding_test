n = int(input())
a = list(map(int, input().split()))
s = int(input())

for i in range(n - 1):
    if s == 0:
        break

    # 가장 큰수 저장하는 변수, 가장 큰 수의 인덱스 -> a[i] 지정, i 지정
    mx, idx = a[i], i

    # 교환할 수 있는 횟수
    for j in range(i + 1, min(n, i + 1 + s)):
        if mx < a[j]:
            mx = a[j]
            idx = j

    s -= idx - i
    for j in range(idx, i, -1):
        a[j] = a[j - 1]
    a[i] = mx

print(*a)

# 바로 다음 수 만을 비교 하는 것이 아닌 현재 위치 보다 뒤에 있는 수 중에서 가장 큰 수와 비교하는 방식으로 풀이해야 함
# https://velog.io/@xx0hn/BOJ-Python-1083%EB%B2%88-%EC%86%8C%ED%8A%B8