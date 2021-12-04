def solution(arr, x):

    min_value = min(arr)
    max_value = max(arr)
    new_arr = []
    new_arr1 = []

    #뺀게 0보다 크면 다 뻄
    for i in range(len(arr)):
        sub = arr[i] - x
        new_arr1.append(arr[i]+x)
        if sub > 0:
            while sub > 0:
                if sub not in arr:
                    sub = sub - x
                else:
                    new_arr.append(sub)
                    break
        else:
            new_arr.append(arr[i])

    max_value = max(new_arr)
    #print(arr, new_arr1)
    if max_value in arr:
        res = check(max_value, arr)
    print(res)
    #return res


def check(value, arr1):
    if value not in arr1:
        return value
    else:
        return check(value+1, arr1)

arr=[1,2,4]
x = 3
solution(arr,x)
#x를 요소에 더하거나 빼서 만든 배열에서 존재하지 않는 원소의 최소값