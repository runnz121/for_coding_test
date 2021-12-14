n = int(input())

memo = [0,1]
def fibo(n):
    global memo
    if n >= len(memo):
        memo.append(fibo(n-2)+fibo(n-1))
    return memo[n]
fibo(n)
print(memo)