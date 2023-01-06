# 根の変更
from collections import deque

N, R = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

K, r = map(int, input().split())

q = deque()
q.append(r - 1)
dist = [-1] * N
dist[r - 1] = 0
while q:
    now = q.popleft()
    for nxt in g[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

for _ in range(K):
    v = int(input())
    v -= 1
    for i in g[v]:
        if dist[i] + 1 == dist[v]:
            print(i + 1)
