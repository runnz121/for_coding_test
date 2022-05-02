import copy

n = int(input())

arr = []

str1 = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
str2 = "\"재귀함수가 뭔가요?\""
str3 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
str4 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
str5 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
str6 = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
str7 = "라고 답변하였지."


arr.append(str2)
arr.append(str3)
arr.append(str4)
arr.append(str5)

delimeter = "____"

arrcp = copy.deepcopy(arr)

def recurse(start, arrr):

    if start == n:
        endstr1 = delimeter * start + str2
        endstr2 = delimeter * start + str6
        arrcp.append(endstr1)
        arrcp.append(endstr2)
        return start
    else:
        for i in arrr:
            i = start*delimeter + i
            arrcp.append(i)
        return recurse(start + 1, arrr)

x = recurse(1, arr)

def recurse1(start):
    if start == 0:
        return
    else:
        addstr = delimeter * start + str7
        arrcp.append(addstr)
        return recurse1(start - 1)
recurse1(x)
arrcp.append(str7)

print(str1)
for i in arrcp:
    print(i)