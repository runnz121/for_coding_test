# def tail(filename, n=10):
#     with open(filename, "r") as f:
#         lines = f.readlines()
#         print("lines", lines)
#     for line in lines.pop(n):
#         print(line)
#
#
# tail("/Users/pupu/Desktop/test.txt")
#
# import re
#
# def parse1():
#     for line in open("/Users/pupu/Desktop/log.txt"):
#         print(line.split("[")[1].split("]")[0])
#
#
# def parse2():
#     for line in open("/Users/pupu/Desktop/log.txt", "r"):
#         print(line.split()[3].strip("[]"))
#
#
# def parse3():
#     for line in open("/Users/pupu/Desktop/log.txt", "r"):
#         print(" ".join(line.split("[" or "]")[3:5]))
#
#
# def parse4():
#     for line in open("/Users/pupu/Desktop/log.txt", "rw"):
#         print(" ".join(line.split()[3:5]).strip("[]"))
#
#
# def parse5():
#     for line in open("/Users/pupu/Desktop/log.txt"):
#         print(re.split("\[|\]", line)[1])
#
# parse5()

# nums = [-1,2,4]
#
# # def sqsum1():
# # 	return sum(x**2 if x > 0 for x in nums)
#
# def sqsum2():
#   	return sum(x^2 for x in nums if x > 0)
#
# # def sqsum3():
# #   	return sum(for x in nums if x > 0 then x^2)
#
# def sqsum4():
#   	return sum(x**2 for x in nums if x > 0)
# #
# # def sqsum5():
# #   	return sum(x^2 if x > 0 for x in nums)
#
# print(sqsum4())

# class FunEvent:
#     def __init__(self, tags, year):
#         self.tags = tags
#         self.year = year
#
#     def __str__(self):
#         return f"FunEvent(tags={self.tags}, year={self.year})"
#
#
# tags = ["google", "ml"]
# year = 2022
# bootcamp = FunEvent(tags, year)
# tags.append("bootcamp")
# year = 2023
# print(bootcamp)

# class BaseLayer:
#     def __init__(self, name=""):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.name}Layer"
#
# class ActivationLayer(BaseLayer):
#     def __init__(self, size):
#         super().__init__("Activation")
#         self.size = size
#
# class FCLayer(BaseLayer):
#     def __init__(self, size):
#         super().__init__("FullyConnected")
#         self.size = size
# print(FCLayer(42))
#
# print(ActivationLayer(23))

x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.extend(y)
print('x:', x)


import heapq

q = [2,4,5,6]
s= []
heapq.heapify(q)

for i in range(4):
    heapq.heappush(s, -q[i])

print(q)
for i in range(4):
    x = heapq.heappop(s)
    print(-x)