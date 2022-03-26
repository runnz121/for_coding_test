# 문제 설명
# 당신은 로그 수집 프로그램을 만들게 되었습니다.
# 특정 조건들을 만족한 로그만을 수집해야 하며 그 외의 로그는 수집하지 않아야 합니다.
#
# 조건은 다음과 같습니다.
#
# 로그는 "team_name : t application_name : a error_level : e message : m" 형식이어야 합니다.
# t, a, e, m은 알파벳 소문자 혹은 알파벳 대문자로만 이루어진 길이 1 이상의 문자열입니다.
# team_name, application_name, error_level, message, :, t, a, e, m는 한 칸의 공백으로 구분되어 있어야 합니다.
# 로그의 길이는 100 이하여야 합니다.
# 로그 수집 프로그램으로 분석할 로그들이 담긴 문자열 배열 logs가 매개변수로 주어졌을 때, logs에 담긴 로그 중 수집하지 않는 로그의 개수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 1 ≤ logs의 길이 ≤ 100
# 1 ≤ logs의 원소 길이 ≤ 200
# logs의 원소는 알파벳, 숫자, 공백, 특수 문자로 이루어져 있습니다.
# 입출력 예
# logs	result
# ["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]	3
# ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]	6
# 입출력 예 설명
# 입출력 예 #1
#
# "team_name : db application_name : dbtest error_level : info message : test"
# 형식에 맞는 로그입니다.
# "team_name : test application_name : I DONT CARE error_level : error message : x"
# application_name 내용에 I DONT CARE이 들어가 있습니다. 공백이 들어가면 안 되므로 수집하지 않는 로그입니다.
# "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever"
# 형식은 맞지만 로그의 길이가 100을 넘어가므로 수집하지 않는 로그입니다.
# "team_name : oberervability application_name : LogViewer error_level : error"
# message 부분이 누락되어 있으므로 수집하지 않는 로그입니다.
# 따라서, 수집하지 않는 로그는 총 3개이므로 3을 return 하면 됩니다.
#
# 입출력 예 #2
#
# "team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange"
# message가 들어가야 할 부분에 e가 빠진 messag가 들어가 있으므로 수집하지 않는 로그입니다.
# "no such file or directory"
# 형식에 전혀 맞지 않으므로 수집하지 않는 로그입니다.
# "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11"
# message 내용에 숫자가 들어있으므로 수집하지 않는 로그입니다.
# "team_name : recommend application_name : recommend error_level : info message : Success!"
# message 내용에 특수문자가 들어있으므로 수집하지 않는 로그입니다.
# "   team_name : db application_name : dbtest error_level : info message : test"
# 가장 앞부분에 공백이 있으므로 수집하지 않는 로그입니다.
# "team_name     : db application_name : dbtest error_level : info message : test"
# team_name 다음에 5개의 공백이 연속해서 들어오므로 수집하지 않는 로그입니다
# "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"
# 형식에 맞는 로그입니다.
# 따라서, 수집하지 않는 로그는 총 6개이므로 6을 return 하면 됩니다.
#
#
def solution(logs):
    answer = 0

    keys = ["team_name", "application_name", "error_level", "message"]
    num = [1,2,3,4,5,6,7,8,9,0]
    db = dict()

    error = []

    for idx in range(len(logs)):
        if len(logs[idx]) > 100:
            id = logs.index(logs[idx])
            answer += 1
            error.append(id)

    error.reverse()
    for err in error:
        del logs[err]


    error = []
    for idx in range(len(logs)):
        logs[idx] = logs[idx].split(' ')
        if len(logs[idx]) != 12:
            id = logs.index(logs[idx])
            answer += 1
            error.append(id)

    error.reverse()
    for err in error:
        del logs[err]


    for i in range(len(logs)):
        match = 0
        for j in range(len(logs[i])):
            if logs[i][j] in keys:
                match += 1
        if match != 3:
            error.append(i)
            print(i)

    error.reverse()
    for err in error:
        del logs[err]


    print(answer)
    print(logs)
    return answer

logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
solution(logs)