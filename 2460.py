people = 0

reduce = 0
for i in range(10):
    x, y = map(int, input().split())
    reduce += y
    reduce -= x
    people = max(people, reduce)
print(people)
