n, k = map(int, input().split())

count = 0
# 물병을 1,1,1,... 로 표현
# 합침 2,2,2,2....
# 결론 : n을 이진수로 바꾼 1의 갯수가 물을 최대로 합친 후의 물병 갯수
while bin(n).count('1') > k:
    n = n+1
    count = count +1

print(count)