from collections import deque

n, r = map(int, input().split())
# 全ての頂点について根である頂点（一番上のノード）からの距離を求め、各辺について、根からの距離が短い方が親、長い方が子であると判定
g = [[] for _ in range(n)]
edge = [list(map(int, input().split())) for _ in range(n-1)]
for i in range(n-1):
    a, b = edge[i]
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(r-1)
dist = [n] * n
dist[r-1] = 0
#幅優先探索で根から各頂点までの距離を求める
while q:
    now = q.popleft()
    for nxt in g[now]:
        if dist[nxt] == n:
            dist[nxt] = dist[now] + 1
            q.append(nxt)
# a_i が b_i の親である場合は "A" を、b_i が a_i の親である場合は "B" を出力            
for i in range(n-1):
    a, b = edge[i]
    a -= 1
    b -= 1
    if dist[a] < dist[b]:
        print("A")
    else:
        print("B")
      
