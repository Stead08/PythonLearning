#木の 2 頂点間の距離
#https://paiza.jp/works/mondai/bfs_dfs_problems/bfs_dfs_problems__length_between_two_vertex

from collections import deque
#頂点の数 N と、頂点番号 X, Y 
N, X, Y = map(int, input().split())
# ツリーを入力を元に作成
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
# 幅優先探索
l = [-1] * N
l[X - 1] = 0
q = deque()
q.append(X - 1)
while q:
    prev = q.popleft()
    for nxt in graph[prev]:
        if l[nxt] == -1:
            l[nxt] = l[prev] + 1
            q.append(nxt)
print(l[Y-1])
