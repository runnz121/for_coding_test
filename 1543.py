a = input()
b = input()
cnt = 0
n = 0
while n <= len(a) - len(b):
    if a[n:n + len(b)] == b: # 찾고자 하는 글자 같은 경우
        cnt += 1
        n += len(b) # 글자가 같음으로 중복되지 않게 다음 인덱스까지 점프
    else:
        n += 1 # 아님으로 인덱스 한칸만 증가
print(cnt)