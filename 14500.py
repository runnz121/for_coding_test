x, y = map(int, input().split())

arr = []

for i in range(x):
    arr.append(list(map(int, input().split())))

ans = 0
square = 0
rectangle1 = 0
rectangle2 = 0
nieun1 = 0
nieun2 = 0
nieun3 = 0
nieun4 = 0
nieun5 = 0
nieun6 = 0
nieun7 = 0
nieun8 = 0
lieul1 = 0
lieul2 = 0
lieul3 = 0
lieul4 = 0
king1 = 0
king2 = 0
king3 = 0
king4 = 0

# 정사각형
for i in range(x):
    for j in range(y):
        if 0 <= i + 1 < x and 0 <= j + 1 < y:
            square = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
        ans = max(square, ans)

# 막대기
for i in range(x):
    for j in range(y):
        if 0 <= i < x and 0 <= j + 3 < y:
            rectangle1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]
        if 0 <= i + 3 < x and 0 <= j < y:
            rectangle2 = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]
        ans = max(rectangle2, rectangle1, ans)

# 니은자
for i in range(x):
    for j in range(y):
        #세로니은
        if 0 <= i + 2 < x and 0 <= j + 1 < y:
            nieun1 = arr[i][j] + arr[i+1][j] + arr[i + 2][j] + arr[i+2][j + 1]
        #역기억
        if 0 <= i + 1 < x and 0 <= j + 2 < y:
            nieun2 = arr[i][j] + arr[i+1][j] + arr[i][j + 1] + arr[i][j+2]
        #기억
        if 0 <= i + 2 < x and 0 <= j + 1 < y:
            nieun3 = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
        #역니은
        if 0 <= i - 1 < x and 0 <= j + 2 < y:
            nieun4 = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+2]
        if 0 <= i - 2 < x and 0 <= j + 1 < y:
            nieun5 = arr[i][j] + arr[i][j + 1] + arr[i-1][j+1] + arr[i-2][j+1]
        if 0 <= i + 1 < x and 0 <= j + 2 < y:
            nieun6 = arr[i][j] + arr[i + 1][j] + arr[i+1][j+1] + arr[i + 1][j+2]
        if 0 <= i + 2 < x and 0 <= j + 1 < y:
            nieun7 = arr[i][j] + arr[i][j+ 1] + arr[i+1][j] + arr[i + 2][j]
        if 0 <= i + 1 < x and 0 <= j + 2 < y:
            nieun8 = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i + 1][j+2]

        ans = max(nieun8, nieun7, nieun6, nieun5, nieun4, nieun3, nieun2, nieun1, ans)

# 리을자
for i in range(x):
    for j in range(y):
        #세로
        if 0 <= i + 2 < x and 0 <=j + 1 < y:
            lieul1 = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i + 2][j+1]
        #가로(1,0)
        if 0 <= i - 1 < x - 1 and 0 <= j + 2 < y:
            lieul2 = arr[i][j] + arr[i][j + 1] + arr[i-1][j+1] + arr[i-1][j+2]

        if 0 <= i + 2 < x and 0 <= j - 1 < y:
            lieul3 = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+2][j-1]

        if 0 <= i + 1 < x and 0 <= j + 2 < y:
            lieul4 = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2]

        ans = max(lieul4, lieul3, lieul2, lieul1, ans)

# 왕관
for i in range(x):
    for j in range(y):
        # 위로 가로
        if 0 <= i - 1 < x and 0 <= j + 2 < y:
            king1 = arr[i][j] + arr[i][j + 1] + arr[i-1][j+1] + arr[i][j + 2]
        # 오른쪽 세로
        if 0 <= i + 2 < x and 0 <=j + 1 < y:
            king2 = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j]
        # 아래쪽 가로
        if 0 <= i + 1 < x and 0 <=j + 2 < y:
            king3 = arr[i][j] + arr[i][j + 1] + arr[i+1][j+1] + arr[i][j+2]
        # 왼쪽 세로
        if 0 <= i - 1 < x - 2 and 0 <= j + 1 < y:
            king4 = arr[i][j] + arr[i][j+1] + arr[i-1][j+1] + arr[i+1][j+1]
        ans = max(king1, king2, king3, king4, ans)

print(ans)