cnt = int(input())
location = list(map(int, input().split()))

location.sort()

print(location[(cnt-1)//2])