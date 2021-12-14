T = int(input())

while T > 0:
    n = int(input())
    memo = [0, 1] # 메모이제이션 사용을 위한 메모 리스트 초기화
    if n == 0:
        print(f'1 0')
    else:
        def fibo(n):
            global memo
            if n >= len(memo): # n 이 0, 1이 아니면
                memo.append(fibo(n - 2) + fibo(n - 1)) # 메모리스트에 해당 값을 인덱스 기준으로 추가
            return memo[n] # 만약 길이보다 작다면 해당 인덱스 값을 바로 반환
        fibo(n)
        print(f'{memo[len(memo)-2]} {memo[len(memo)-1]}')
    T -=1
