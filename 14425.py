class Node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.child = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.child:
                curr_node.child[char] = Node(char) # foo가 들어온다고하면 -> f : {} ->  f : { o : {}} -> f: {o : { o {}}} ->
            curr_node = curr_node.child[char] # -> f를 키 값으로 갖고있는 dict를 지정함 -> o를 키값으로 갖고 있는 dict를 지정함 -> o를 키값으로 갖고있는 dict를 지정함 ->
        curr_node.data = string # f:{o:{o: foo }}}

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.child:
                curr_node = curr_node.child[char]
            else:
                return False
        if curr_node.data:
            return True
        else:
            return False

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trie = Trie()
count = 0

for i in range(n + m):
    string = input().rstrip()
    if i < n:
        trie.insert(string)
    else:
        if trie.search(string):
            count += 1
print(count)