# https://paiza.jp/works/mondai/graph_dfs_problems/graph_dfs__tree_step5
n = int(input())
ad_list = {}
start = []
for i in range(1, n + 1):
    v = int(input())
    if v == 1:
        start.append(i)
    ad_list[i] = list(map(int, input().split()))


def dfs(v, visited):
    if len(visited) == n:
        for i in range(n - 1):
            print(visited[i], visited[i + 1])
        exit()
    else:
        for i in ad_list[v]:
            if i not in visited:
                visited.append(i)
                dfs(i, visited)
                visited.pop()


if len(start) > 2:
    print("-1")
elif len(start) > 0:
    dfs(start[0], [start[0]])
    print("-1")
else:
    for i in range(1, n + 1):
        dfs(i, [i])
    print("-1")
