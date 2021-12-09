import sys
T = int(input())
arr = []
for i in range(T):
    a, b = sys.stdin.readline().split()
    arr.append((int(a),b,i)) # 나이는 인트로

arr = sorted(arr, key = lambda x : (x[0], x[2]))

for i in range(T):
    print(f'{arr[i][0]} {arr[i][1]}')