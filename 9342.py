import re

p = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(int(input())):
    print('Good' if p.match(input()) is None else 'Infected!')
