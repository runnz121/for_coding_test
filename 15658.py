import sys

n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_amt = -sys.maxsize
min_amt = sys.maxsize


def cal(tot, idx):
    global max_amt
    global min_amt

    if idx == len(nums):
        max_amt = max(max_amt, tot)
        min_amt = min(min_amt, tot)
        return

    if operator[0] != 0:
        operator[0] -= 1
        cal(tot + nums[idx], idx + 1)
        operator[0] += 1

    if operator[1] != 0:
        operator[1] -= 1
        cal(tot - nums[idx], idx + 1)
        operator[1] += 1

    if operator[2] != 0:
        operator[2] -= 1
        cal(tot * nums[idx], idx + 1)
        operator[2] += 1

    if operator[3] != 0:
        operator[3] -= 1
        cal(int(tot / nums[idx]), idx + 1)
        operator[3] += 1


cal(nums[0], 1)

print(max_amt)
print(min_amt)