array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #리스트가 하나 이하라면 종료(재귀 종료조건)
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗의 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left = [x for x in tail if x <= pivot] # 분할된 왼쪽
    print("left", left)
    right = [x for x in tail if x > pivot] # 분할된 오른쪽
    print("right", right)

    #분할 이후 왼쪽과 오른쪽에서 각각 정렬 수행, 리스트 반환
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))