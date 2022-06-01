l, r = map(int, input().split())
strL = str(l)
strR = str(r)

cnt = 0

# 두 숫자 길이 다르면 무조건 0
if len(strL) != len(strR):
    print(0)
else:
    # 길이가 같을 때
    # 1. 두 숫자 값이 다른 경우 0
    # 2. 일부값이 같을 때 8을 제외하고 나머지 자리는 8을 포함하지 않을 수 있음 : 1
    # 3. 두 숫자 값이 같을 때 포함하는 8 세기
    for i in range(len(strR)):
        if strL[i] != strR[i]: #
            break
        else:
            if strL[i] == '8':
                cnt += 1
    print(cnt)