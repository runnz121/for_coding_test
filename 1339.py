n = int(input())

arr = []
max_length_word = 0
db = dict()
char_idx = dict()
number = [False] * 11
number[0] = True

for i in range(n):
    x = str(input())
    str_len = len(x)
    # 단어와 단어 길이 저장
    arr.append([x, str_len])

# 가장 길이가 긴 문자열을 찾기 -- 1 우선순위
def find_longest_string():
    global arr

    # 긴 길이로 역순 정렬
    arr.sort(key = lambda x : -x[1])


# 입력받은 글자 인덱싱 및 갯수 갱신
def index_dict():
    global arr
    global db

    for i in arr:
        for k in range(len(i[0])):
            if i[0][k] not in db:
                db[i[0][k]] = 1
            else:
                db[i[0][k]] += 1

    db = sorted(db.items(), key = lambda x : x[1], reverse=True)
    return db

index_dict()
print(db)