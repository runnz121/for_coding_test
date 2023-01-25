N = int(input())
a = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if a[i] < a[i-1]: # 전의 자리가 더 큰 경우
        x, y = i-1, i # 두 자리 술 ㄹ바꿈
        for j in range(N-1, 0, -1): # 나머지 수중
            if a[j] < a[x]:
                a[j], a[x] = a[x], a[j]
                a = a[:i] + sorted(a[i:], reverse=True) # 내림차순 정렬
                print(*a)
                exit(0)
print(-1)