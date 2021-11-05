n = int(input())
array = list(map(int, input().split()))

#인덱스 기준
start = 0
end = n-1

def search(array, start, end):

    if start > end:
        return None

    mid = (start + end) //2

    if array[mid] == mid:
        return mid

    elif array[mid] < mid:
        return search(array, mid+1, end)

    else:
        return search(array, start, mid-1)

#이부분이 추가됨
index = search(array, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)