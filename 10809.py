sts = str(input())
db = dict()
table = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
check  =[]

#dict 초기화
for i in range(len(table)):
    db[table[i]] = -1

for i in range(len(sts)):
    if sts[i] not in check:
        db[sts[i]] += i+1
        check.append(sts[i])

#출력
for i in range(len(table)):
    print(db[table[i]], end=' ')

#dict 이용해서 알파벳과 순서 묶어서 value값에 해당 인덱스 번호 저장, 체크 배열 만들어서 이미 있는 경우 해당 원소 제거거