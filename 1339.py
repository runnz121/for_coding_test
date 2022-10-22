n = int(input())

arr = []
max_length_word = ''
db = dict()

for i in range(n):
    x = str(input())
    arr.append(x)

# 가장 길이가 긴 문자열을 찾기 -- 1 우선순위
def find_longest_string():

    global max_length_word

    for i in arr:
        if len(i) > len(max_length_word):
            max_length_word = i

    return max_length_word


# 중복되는 글자수가 많은 것을 찾기 -- 2
def find_most_duplicated(str):
    




# 입력받은 글자 인덱싱 및 갯수 갱신
def index_dict():
    global arr
    global db

    for i in arr:
        for k in range(len(i)):
            if i[k] not in db:
                db[i[k]] = 1
            else:
                db[i[k]] += 1

    db = sorted(db.items(), key = lambda x : x[1], reverse=True)
    return db
