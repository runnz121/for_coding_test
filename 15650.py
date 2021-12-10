a, b = map(int, input().split())
arr = []
ans = []
def back1(depth):
    if depth == b:
        cc = sorted(arr)
        if cc not in ans: # 확인 배열 하나더 추가해서 없으면 출력 아니면 걍 종료
            ans.append(cc)
            print(' '.join(map(str, cc)))
        else:
            return
        return
    for i in range(1, a+1):
        if i not in arr:
            arr.append(i)
            back1(depth+1)
            arr.pop()
back1(0)