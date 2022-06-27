n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

dp = [0] * (n+1)
cnt = 0
def fibo(n):
    dp[1] = 1
    dp[2] = 1
    global cnt

    for i in range(3, n):
        cnt += 1
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

fibo(n)

print(fib(n), cnt+1)
