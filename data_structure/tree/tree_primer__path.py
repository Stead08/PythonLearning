from collections import deque
n, A, B = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

distance = [n] * n
distance[a-1] = 0
q = deque()
q.append(a-1)

l = [-1] * n
l[A - 1] = 0
q = deque()
q.append(A - 1)
prev = [-1] * n
while q:
    now = q.popleft()
    if now == B - 1:
        break
    for nxt in g[now]:
        if l[nxt] == -1:
            l[nxt] = l[now] + 1
            prev[nxt] = now
            q.append(nxt)

tmp = B - 1
ans = []
#各頂点 V_i について頂点 X から V_i への最短経路における V_i の 1 つ前の頂点を記憶しておき、頂点 Y から順に 1 つ前の頂点をたどっていくことで最短経路の逆順を得る
while tmp != -1:
    ans.append(tmp)
    tmp = prev[tmp]
for i in ans[::-1]:
    print(i + 1)
