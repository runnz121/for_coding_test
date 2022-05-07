def solution(survey, choices):
    arr = []

    db = {'A': 0, 'N': 0, 'J': 0, 'M': 0, 'C': 0, 'F': 0, 'R': 0, 'T': 0, }

    answer = ''

    for i in survey:
        arr.append(list(i))

    for k in range(len(choices)):
        if choices[k] >= 4:
            db[survey[k][1]] += 3 - (7 - choices[k])
            # print(survey[k][1], db[survey[k][1]])

        elif choices[k] <= 4:
            db[survey[k][0]] += 4 - choices[k]


    #1
    if db['R'] != 0 or db['T'] != 0:
        if db['R'] == db['T']:
            answer += 'R'

        elif db['R'] > db['T']:
            answer += 'R'
        else:
            answer += 'T'
    else:
        answer += 'R'
    #2
    if db['C'] != 0 or db['F'] != 0:
        if db['C'] == db['F']:
            answer += 'C'
        elif db['C'] > db['F']:
            answer += 'C'
        else:
            answer += 'F'
    else:
        answer += 'C'
    #3
    if db['J'] !=0 or db['M'] != 0:
        if db['J'] == db['M']:
            answer += 'J'
        elif db['J'] > db['M']:
            answer += 'J'
        else:
            answer += 'M'
    else:
        answer += 'J'
    #4
    if db['A'] != 0 or db['N'] != 0:
        if db['A'] == db['N']:
            answer += 'A'
        elif db['A'] > db['N']:
            answer += 'A'
        else:
            answer += 'N'
    else:
        answer += 'A'

    return answer




survey = ["TR", "RT", "TR"]
choice = [7, 1, 3]
solution(survey, choice)
