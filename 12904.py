import sys

input = sys.stdin.readline

string = str(input().rstrip())
check = str(input().rstrip())


def first(string):
    res = string + 'A'
    return res

def second(string):
    res = string[::-1] + 'B'
    return res


first(string)
second(string)
print(string)