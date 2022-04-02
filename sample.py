import math

n = 1000

check = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n) + 1)):
	if check[i] == True:
		j = 2
		while i * j <= n:
			check[i * j]  = False
			j += 1