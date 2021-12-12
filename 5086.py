
decision = ["factor", "multiple", "neither"]

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b :
        if a % b == 0 :
            ans = decision[1]
        else:
            ans = decision[2]
    else:
        ans = decision[0]
    print(ans)