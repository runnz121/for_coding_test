n = int(input())

def fibo(x):
    if x <= 1:
        return x
    return fibo(x-1) + fibo(x-2)
print(fibo(n))

#fibo(9) + fibo(8)

#fibo(8) + fibo(7) + fibo(7) + fibo(6)

#fibo(2) -> fibo(1) + fibo(0) -> 1, 0 -> fibo(2) - > 1