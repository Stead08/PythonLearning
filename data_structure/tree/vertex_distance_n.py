from collections import deque
n, a, x = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    g[A].append(B)
    g[B].append(A)

distance = [n] * n
distance[a-1] = 0
q = deque()
q.append(a-1)

while q:
    now = q.popleft()
    for nxt in g[now]:
        if distance[nxt] == n:
            distance[nxt] = distance[now] + 1
            q.append(nxt)

ans = []

for i, dist in enumerate(distance):
    if dist == x:
        ans.append(i+1)
        
for i in sorted(ans):
    print(i)
