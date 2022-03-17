a, b = map(int, input().split())
arr = list(input().split())
check =[False] * b
vowles = ['a','e','i','o','u']
arr.sort()

string = ""

def back(depth, start):

   # print(check)

    global string
    if depth == a:
        vali(string) # 모음 1개, 자음 2개일 경우 조건
        return

    for i in range(start, b):
        if check[i]:  # 이미 방문 처리가 되어있다면 패스 그게 아니라면,
            continue
        check[i] = True # 해당 인덱스를 방문 처리
        string += arr[i] # 주어진 배열의 값을 문자열열에 더함
        back(depth + 1, i) # 뎁스 하나 증가와, 해당 인덱스를 시작 시점으로 넣음
        string = string[:-1] # 문자열의 맨 끝값을 제외한것을 문자로 함
        check[i] = False # 체크 배열을 다시 풀어줌

def vali(string):

    vow_count = 0
    cons_count = 0
    for i in range(len(string)):
        if string[i] in vowles:
            vow_count += 1
        else:
            cons_count += 1
        if i == len(string) - 1:
            if vow_count >= 1 and cons_count >= 2:
                print(string)
back(0,0)