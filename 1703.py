while 1:
    list_ = list(map(int, input().split()))
    leaf = 1 #구하고자 하는 나뭇잎 개수
    if list_[0] == 0: #0을 입력받으면 while문에서 탈출한다.
        break

    for i in range(1, len(list_), 2):
        leaf = leaf * list_[i] - list_[i+1]
    print(leaf)