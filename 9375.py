from collections import Counter

#(의상 종류의 개수 + 1) * (의상 종류의 개수 + 1) * ... -1 을 해주면 된다.
t = int(input())
for i in range(t):
    n = int(input())
    s = []
    for j in range(n):
        a, b = input().split()
        s.append(b)
    num = 1
    result = Counter(s)
    for key in result:
        num *= result[key] + 1
    print(num - 1)