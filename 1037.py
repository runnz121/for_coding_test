T = int(input()) #어떤수의 약수 갯수
arr = list(map(int, input().split())) # 어떤수의 약수

arr.sort()

if len(arr)==1:
    ans = arr[0]**2
else:
    ans = min(arr) * max(arr)

print(ans)