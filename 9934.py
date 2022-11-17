n = int(input())
tree = list(map(int, input().split()))

# root node를 구함
def root_nodes(nodes):
    return nodes[len(nodes)//2]

print_arr= []


def recurse(nodes, depth):
    if depth == n:
        return

    if len(nodes) <= 1:
        print_arr.append([nodes[0], depth])
        return

    root_node = root_nodes(nodes)
    print_arr.append([root_node, depth])

    recurse(nodes[:len(nodes)//2], depth + 1)
    recurse(nodes[len(nodes)//2:], depth + 1)

recurse(tree, 0)


print_arr = sorted(print_arr, key = lambda x : x[1])


for i in range(n):
    prints= []
    for node in print_arr:
        if node[1] == i:
            prints.append(node[0])
    print(*prints)

# 4
# 8 2 9 4 10 1 11 5 12 6 13 3 14 7 15