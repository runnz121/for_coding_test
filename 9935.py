import sys

sys.setrecursionlimit(10 ** 4)

input = sys.stdin.readline

string = str(input().rstrip())
comp = str(input().rstrip())

def recur(string):
    if comp in string:
        str = string.replace(comp, "")
    else:
        return string

    if comp in str:
        return recur(str)
    return str

res = recur(string)

if res == "":
    print("FRULA")
else:
    print(res)
