n, m = map(int, input().split())


# 2, 5 쌍의 갯수를 구하면 된다

# 들어온 수의 2의 배수의 갯수를 구하는 공식
def two(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two


def five(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five


#nCr = n! / ((n-k)! * k!)
# 2와 5의 갯수를 각각 구하고 최소값을 출력
# 위의 공식을 참고하여
# n!이 갖고 있는 2의 갯수 - (n-k)!이 갖고 있는 2의 갯수 - m!이 갖고 있는 2의 갯수
# n!이 갖고 있는 5의 갯수 - (n-k)!이 갖고 있는 5의 갯수 - m!이 갖고 있는 5의 갯수
print(min(two(n) - two(n - m) - two(m), five(n) - five(n - m) - five(m)))
