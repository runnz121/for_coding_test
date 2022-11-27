def solution(s, times):
    answer = []
    s = list(s.split(":"))

    acc_time = []
    for i in times:
        i = list(i.split(":"))
        acc_time.append(i)

    # # 저축 기간 정렬
    # acc_time = sorted(acc_time, key = lambda x : (x[0], x[1], x[2], x[3]))

    filter_arr = []

    cur = s
    for acc in acc_time:
        # 보정값
        mins = 0
        hours = 0
        days = 0
        month = 0
        year = 0

        # 초
        if int(acc[3]) + int(cur[5]) >= 60:
            mins += 1
            cur_s = int(acc[3]) + int(cur[5]) - 60
        else:
            cur_s = int(acc[3]) + int(cur[5])

        # 분
        if int(acc[2]) + int(cur[4]) >= 60:
            hours += 1
            cur_mi = int(acc[2]) + int(cur[4]) - 60 + mins
        elif int(acc[2]) + int(cur[4]) + mins >= 60:
            hours += 1
            cur_mi = int(acc[2]) + int(cur[4]) + mins
        else:
            cur_mi = int(acc[2]) + int(cur[4]) + mins

        # 시간
        if int(acc[1]) + int(cur[3]) >= 24:
            days += 1
            cur_h = int(acc[1]) + int(cur[3]) - 24 + hours
        elif int(acc[1]) + int(cur[3]) + hours >= 24:
            days += 1
            cur_h = int(acc[1]) + int(cur[3]) + hours
        else:
            cur_h = int(acc[1]) + int(cur[3]) + hours

        # 일
        if int(acc[0]) + int(cur[2]) >= 31:
            month += 1
            cur_d = int(acc[0]) + int(cur[2]) - 30 + days
        elif int(acc[0]) + int(cur[2]) + days >= 31:
            month += 1
            cur_d = int(acc[0]) + int(cur[2]) + days
        else:
            cur_d = int(acc[0]) + int(cur[2]) + days

        # 달
        if int(cur[1]) + month >= 13:
            cur_m = int(cur[1]) + month - 12
            year += 1
        else:
            cur_m = int(cur[1])
        # 연
        cur_y = int(cur[0]) + year

        cur[5] = cur_s
        cur[4] = cur_mi
        cur[3] = cur_h
        cur[2] = cur_d
        cur[1] = cur_m
        cur[0] = cur_y

        filter_arr.append([cur[0], cur[1], cur[2]])

    filter_arr = sorted(filter_arr, key = lambda x : (x[0], x[1], x[2]))

    # 저축기간
    tot_days = len(filter_arr)



    # 날짜
    if filter_arr[len(filter_arr)-1][2] - s[2] < 0:
        if filter_arr[len(filter_arr)-1][1] - 1 < 0:
            filter_arr[len(filter_arr)-1][0] - 1





    return answer


s = "2021:04:12:16:08:35"
times = ["01:06:30:00", "01:04:12:00"]
solution(s, times)