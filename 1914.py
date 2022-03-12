n = int(input())

# from, to , middle 이 있다.
# 이것들은 처음그냥 고정

ans = []

#시작은 고정이다 따라서 조건은 그대로인데, 옮기는 목적지만 다르게 적용되는 재귀
def hanoi(n, _from, _to, _middle):
    if (n == 1):
        print(_from, _to)
#        ans.append([_from, _to])
        return
    # 맨 처음 n-1 개 만큼 middle 로 옮긴다
    hanoi(n-1, _from, _middle, _to)
    print(_from, _to)
   # ans.append([_from, _to])
    # middle에서 n-1개 만큼 to로 옮긴다
    hanoi(n-1, _middle, _to, _from)
# hanoi(n, 1, 3, 2)

print(2**n-1)
if n <= 20:
    hanoi(n, 1, 3, 2)