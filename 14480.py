a, b = map(int, input().split())
money = int(input())

if (a + b) >= 2 * money:
    print((a + b) - 2 * money)
else:
    print(a + b)