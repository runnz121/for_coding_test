from itertools import permutations, combinations

string = str(input())

lens = len(string)

arr = [i+1 for i in range(lens-1)]


s = list(combinations(arr, 2))


ans = []

for i in s:
    ans.append(string[:i[0]][::-1] + string[i[0]:i[1]][::-1] + string[i[1]:][::-1])

ans.sort()

print(ans[0])