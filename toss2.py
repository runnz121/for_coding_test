import decimal
def solution(levels):
    lens = len(levels)
    if lens == 1:
        return levels[0]

    top = lens * 0.75
    top = decimal.Decimal(top)
    top = round(top)
    top = int(top)

    levels.sort()
    answer = levels[top]


    return answer

print(solution([1]))
print(solution([1,2,3,4,5,6,7,8,9]))