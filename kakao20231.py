def solution(today, terms, privacies):
    answer = []

    # 약관을 분리
    termDB = dict()
    for i in terms:
        x = i.split(' ')

        if x[0] not in termDB:
            termDB[x[0]] = int(x[1])

    # 오늘 날짜를 각 분리
    today = today.split('.')

    today_year = int(today[0])
    today_month = int(today[1])
    today_day = int(today[2])

    idx = 0
    # 약관을 바탕으로날짜를 계산
    while True:
        if idx >= len(privacies):
            break

        i = privacies[idx]

        # 날짜와 약관을 분리
        temp = i.split(' ')

        # 해당 날의 약관을 추출
        theTerm = temp[1]

        # 날짜별로 분리
        date = temp[0].split('.')

        # 년을 추출
        year = int(date[0])

        # 날짜에서 달을 추출
        month = int(date[1])

        # 일을 추출
        day = int(date[2])

        # print(year,month,day)

        # 보관 날짜를 계산
        toAddMonth = termDB[theTerm]
        month += toAddMonth

        # 달이 12보다 크면 그만큼 년을 높임
        if month > 12:
            year = year + month // 12

            month = month % 12

        if month == 0:
            month = 12
            year -=1

        # day를 보정
        day -= 1
        if day == 0:
            month -= 1
            day = 28

        if month == 0:
            month = 12
            year -= 1

        print(year, month, day)
        idx += 1

        flag = False
        if today_year > year:
            answer.append(idx)
        elif today_year == year:
            pass
        else:
            flag = True

        if today_month > month and flag == False:
            answer.append(idx)
            flag = True
        elif today_month == month:
            pass
        else:
            flag = True

        if today_day > day and flag == False:
            answer.append(idx)

    answer = set(answer)
    answer = list(answer)
    answer.sort()
    print(answer)
    return answer


today = "2020.02.01"
terms = ["Z 12", "D 5"]
privacies = ["2018.12.28 Z"]
solution(today, terms, privacies)
