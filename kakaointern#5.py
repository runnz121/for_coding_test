def solution(tree_nodes, tree_from, tree_to):
    ans = []
    graph = [[] for _ in range(tree_nodes+1)]
    for i in range(1,tree_nodes):
        froms = tree_from[i-1]
        tos = tree_to[i-1]
        graph[froms].append(tos)

    #print(graph)
    for j in range(len(graph)): # j=1
        for x in range(len(graph[j])): # j=1, x = 2,6,7
            if j not in graph[graph[j][x]]:
                graph[graph[j][x]].append(j)

    lens = len(graph)
    for k in range(1, lens):
        print(graph[k])
        if len(graph[k]) == 1:
            ans.append(1)
        else:
             #print(0, end =' ')
            ans.append(0)
    print(ans)
    #
    #print(graph)
    #return 0



tree_nodes = 7
tree_from = [1, 2, 3, 3, 1, 1]
tree_to = [2, 3, 4, 5, 6, 7]
solution(tree_nodes, tree_from, tree_to)