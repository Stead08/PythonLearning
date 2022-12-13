#https://paiza.jp/works/mondai/bfs_dfs_problems/bfs_dfs_problems__route_between_two_vertex
from collections import deque
#ツリーの中のに頂点の最短距離を求める
#木における幅優先探索によって求まる 2 頂点間の距離は最短であることが保証されているため、 
#頂点 X から幅優先探索をおこない頂点 Y までの距離を求めることで頂点 X, Y 間の最短距離を求めることができる
N, X, Y = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

l = [-1] * N
l[X - 1] = 0
q = deque()
q.append(X - 1)
prev = [-1] * N
while q:
    now = q.popleft()
    if now == Y - 1:
        break
    for nxt in graph[now]:
        if l[nxt] == -1:
            l[nxt] = l[now] + 1
            prev[nxt] = now
            q.append(nxt)

tmp = Y - 1
ans = []
#各頂点 V_i について頂点 X から V_i への最短経路における V_i の 1 つ前の頂点を記憶しておき、頂点 Y から順に 1 つ前の頂点をたどっていくことで最短経路の逆順を得る
while tmp != -1:
    ans.append(tmp)
    tmp = prev[tmp]

for i in ans[::-1]:
    print(i + 1)
