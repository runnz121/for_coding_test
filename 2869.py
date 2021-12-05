import math
a, b, c = map(int, input().split())
day = (c - b) / (a - b)
print(math.ceil(day))
# https://lordofkangs.tistory.com/104

#터치다운은 낮에 일어남
# n - 1 >= (V - A) / (A - B)
# n >= (V - A) / (A - B) + 1
# n >= (V - A) / (A - B) + (A - B) / (A - B)
# n >= (V - B) / (A - B)

# int days = (V - B) / (A - B);