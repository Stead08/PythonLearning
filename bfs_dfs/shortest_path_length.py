from collections import deque

N, M, X, Y = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

for i in range(N):
    graph[i].sort()

q = deque()
q.append(X - 1)
l = [-1] * N
l[X - 1] = 0
while q:
    now = q.popleft()
    for nxt in graph[now]:
        if l[nxt] == -1:
            l[nxt] = l[now] + 1
            q.append(nxt)
print(l[Y - 1])
