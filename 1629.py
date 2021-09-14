import math

def power(a, b):
    if b==1:
        return a%c
    else:
        temp = power(a,b // 2)
        if b%2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c

if __name__ == "__main__":
    a, b, c = map(int, input().split())

    result = power(a,b)
    print(result)
