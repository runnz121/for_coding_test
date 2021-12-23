import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
greedy = []
for i in nums:
    s = str(i)
    leng = len(s)

    while len(s) < 10:
        s += s[len(s)-leng]
    # print(s)
    greedy.append(([*list(s)],str(i)))
    print(greedy)
greedy.sort(key = lambda x : x[0], reverse = True)

ans = ""
for i in greedy:
    ans += i[-1]
print(ans if int(ans) != 0 else 0)