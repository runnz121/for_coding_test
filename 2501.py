a, b = map(int, input().split())

div = []

for i in range(1, a + 1):
    if a%i == 0:
        div.append(i)

#div = set(div)
div = list(div)
div.sort()

#print(div)

if len(div)>=b:
    print(div[b-1])
else:
    print(0)