from collections import deque

n = int(input())

# 배우 수
act = [i for i in range(1, n+1)]

check = [False] * n

stage = deque()

scene = n + 1


stage.append(act[0])


def recurse(idx):
    if idx == n:
        return

    # 무대에 사람이 있는 경우
    if len(stage) == 1:
        # 다음 순번을 출력
        print(act[idx])
        stage.append(act[idx])
    # 무대에 2명이 있을 경우
    elif len(stage) == 2:
        # 이전에 있던 사람을 내보냄
        print(stage.popleft())

    recurse(idx + 1)


print(scene)
print(act[0])
recurse(1)
while stage:
    print(stage.popleft())