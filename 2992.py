n = list(str(input()))

ans = []

comp = []

check = [False] * len(n)

def back(depth):

    global ans
    global comp

    if depth == len(n):
        if int("".join(ans)) > int("".join(n)):
            comp.append(int("".join(ans)))
        return

    for i in range(len(n)):
        if check[i]:
            continue

        check[i] = True
        ans.append(n[i])
        back(depth + 1)
        ans.pop()
        check[i] = False
back(0)

comp.sort()

if len(comp) > 0:
    print(comp[0])
else:
    print(0)