x,y,w,h = map(int, input().split())

a = min(x-0, y-0)
b = min(w-x, h-y)

print(min(a,b))