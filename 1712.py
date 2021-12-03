a,b,c = map(int,input().split())

for i in range(2100000000):
    if c - b > 0:
        ans = a//(c-b)
        print(ans+1)
        break
    else:
        print(-1)
        break