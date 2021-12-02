strs = str(input())

if strs ==  " ":
    count = 0
else:
    count = 1
lens = len(strs)

if strs[0] and strs[len(strs)-1] == " ":
    strs = strs[1:-1]
elif strs[len(strs)-1] == " ":
    strs = strs[:-1]
elif strs[0] == " ":
    strs = strs[1:]
else:
    strs = strs

for i in range(len(strs)):
    if strs[i] == " ":
        count += 1
print(count)