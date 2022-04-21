import copy

n = int(input())


cp = copy.deepcopy(n)

def recurse(n):
    init = str(n)
    ls = list(init)
    for i in range(len(init)-1, -1,-1):
        if int(ls[i]) >= 7:
            ls[i] = "7"
        else:
            ls[i] = "4"
    return ls
var = recurse(n)


n_rev = int("".join(var))

while n_rev <= cp:
    n_rev = recurse(n_rev)

print(n_rev)

# if n_rev > cp:
#     n -= 1
#     recurse(n)
# else:
#     print(n_rev)
#     exit()

# xis = int("".join(xis))
# print(xis)
