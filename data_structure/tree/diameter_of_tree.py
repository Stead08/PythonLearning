# 木の直径を求める
from collections import deque
n = int(input())
g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

def bfs(s):
    dist = [-1] * n
    dist[s] = 0
    q = deque()
    q.append(s)
    while q:
        now = q.popleft()
        for nxt in g[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)
    
    return dist
# 適当な頂点から最も遠い頂点Vを探す
dist_from_zero = bfs(0)
max_dist = max(dist_from_zero)
# Vから最も遠い頂点への距離を求める
for i, j in enumerate(dist_from_zero):
    if j == max_dist:
        diameter = max(bfs(i))
        print(diameter)
        break
