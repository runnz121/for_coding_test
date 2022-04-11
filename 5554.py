arr = []

for i in range(4):
    arr.append(int(input()))


res = sum(arr)

print(res//60)
print(res%60)