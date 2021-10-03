x = input()

cnt = 0

row = int(x[1]) #가로
column = int(ord(x[0]) - ord('a')) #세로

steps = [(2,1),(2,-1),(-2,1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2)]


for step in steps:
    next_row = row+step[0]
    next_column = column + step[1]
    if next_row >=1 and next_row <= 8 and next_column>=1 and next_column <= 8:
        cnt+=1
print(cnt)