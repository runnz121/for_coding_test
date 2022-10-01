N, M, K = map(int, input().split())
print(min(M, K) + N - max(M, K)) #둘 중 작은 것 + 둘 중 큰 것