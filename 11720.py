count = int(input())
elements = int(input())

ans = 0
for i in range(count):
    ans += elements % 10
    elements = elements//10

print(ans)

#10으로 계속 나눠서 나머지를 더함