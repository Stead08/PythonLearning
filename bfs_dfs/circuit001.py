# 閉路を一つ出力
# https://paiza.jp/works/mondai/graph_dfs_problems/graph_dfs__cycle_step1
n, s = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

path = []
def dfs (v, visited):
    for i in ad_list[v]:
        if i == s and len(visited) > 2:
            visited.append(i)
            print(*visited)
            exit()
        elif i not in visited:
            visited.append(i)
            dfs(i, visited)
            visited.pop()
if len(ad_list[s]) == 1:
    print(-1)
else:
    dfs(s, [s])
    print(-1)
