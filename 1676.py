T = int(input())

def recur(T):
    if T == 1:
        return 1
    return T * recur(T-1)
if T == 0:
    cnt = 0
else:
    strs = recur(T)
    cnt = 0
    strs = str(strs)
    #print(strs)
    for k in range(len(strs)-1, 0, -1):
        #print('k',strs[k])
        if strs[k] == '0':
            cnt += 1
        else:
            break
print(cnt)