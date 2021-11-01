array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:  #원소가 1개인 경우
        return

    pivot = start #처음시작시 피벗은 첫번째
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 right -= 1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        print(array)
    quick_sort(array, start, right - 1)
    quick_sort(array,right + 1, end)
quick_sort(array, 0, len(array) - 1)

print(array)