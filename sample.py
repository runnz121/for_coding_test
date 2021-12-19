def found(keypad, tofound):
    answer = []
    for i in range(4):
        for j in range(3):
            if tofound == keypad[i][j]:
                answer.append((i,j))
    return answer




def solution(numbers, hand):
    left = ['*', '1', '4', '7']

    for i in range(len(numbers)):
        if str(numbers[i]) in left:
            print(numbers[i])

    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    answer = found(keypad, 8)

    print(answer[0][0])
    return answer

numbers =[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers1=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand ="right"
hands="left"
solution(numbers, hand)