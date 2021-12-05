n = int(input())

line = 0
end = 0
while n > end: # 대각선으로 봤을때 내가 원하는 수가 몇번째 라인(레벨)에 있는지 확인
    line += 1
    end += line

diff = end - n
if line % 2 == 0: # 해당 라인이 짝수이면 분자는 1씩 증가, 분모는 1씩 감소
    top = line - diff
    bottom = diff + 1
else: # 홀수는 분자는 1씩 감소, 분모는 1씩 증가가
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top, bottom))