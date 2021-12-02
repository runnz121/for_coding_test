sts = str(input())
count = 0
arr = ["dz=","d-","c=","c-","lj","nj","s=","z="]

for i in sts:
    for j in range(len(arr)):
        if arr[j] in sts:
            sts = sts.replace(arr[j],' ')
            count = sts.count(' ')

rest = 0
for i in range(len(sts)):
    if " " not in sts[i]:
        rest += 1
print(rest + count)