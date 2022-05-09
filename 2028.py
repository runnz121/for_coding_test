n = int(input())

for k in range(n):

    N = int(input())

    N_square = str(N * N)

    N_length = len(str(N))

    if N_square[-N_length:] == str(N):
        print("YES")
    else:
        print("NO")