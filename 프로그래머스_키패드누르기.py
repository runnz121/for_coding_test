def found(keypad, tofound):
    answer = []
    for i in range(4):
        for j in range(3):
            if tofound == keypad[i][j]:
                answer.append((i,j))
    return answer


def solution(numbers, hand):
    answer = ''
    left = ['*', '1','4','7']
    right = ['#', '3','6','9']
    mid = ['2','5','8','0']
    keypad = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['*','0','#']
              ]
    lp = left[0]
    rp = right[0]

    for i in range(len(numbers)):
        if str(numbers[i]) in left:
            answer += 'L'
            lp = str(numbers[i])

        if str(numbers[i]) in right:
            answer += 'R'
            rp = str(numbers[i])

        if str(numbers[i]) in mid:
            mida = found(keypad, str(numbers[i]))
            lpa = found(keypad, lp)
            rpa = found(keypad, rp)
            print(mida,numbers[i], lpa, rpa)

            if (abs(mida[0][0] - lpa[0][0]) + abs(mida[0][1]-lpa[0][1])) == (abs(mida[0][0] - rpa[0][0]) + abs(mida[0][1] - rpa[0][1])):
                if hand == 'right':
                    answer += 'R'
                    rp = keypad[mida[0][0]][mida[0][1]]
                else:
                    answer += 'L'
                    lp = keypad[mida[0][0]][mida[0][1]]
            elif (abs(mida[0][0] - lpa[0][0]) + abs(mida[0][1] - lpa[0][1])) > (abs(mida[0][0] - rpa[0][0]) + abs(mida[0][1] - rpa[0][1])):
                answer += 'R'
                rp = keypad[mida[0][0]][mida[0][1]]
            else:
                answer += 'L'
                lp = keypad[mida[0][0]][mida[0][1]]

       # print(lp, rp)
    #print(answer)
    return answer


numbers =[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers1=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand ="right"
hands="left"
solution(numbers1, hands)

# LRLLLRLLRRL
# LRLLLRL