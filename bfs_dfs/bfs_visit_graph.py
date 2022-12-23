# https://paiza.jp/works/mondai/bfs_dfs_problems/bfs_dfs_problems__bfs_visit_graph
from collections import deque

n, m, x = map(int, input().split())
#グラフの枠組みを作成
graph = [[] for _ in range(n)]
#入力
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
for i in range(n):
    graph[i].sort()

q = deque()
q.append(x-1)
unvisited = [True] * n
unvisited[x-1] = False
while q:
    now = q.popleft()
    print(now + 1)
    for nxt in graph[now]:
        if unvisited[nxt]　 == True:
          #　もし訪れていなかったら訪れて、unvisitedをFalseにする
            unvisited[nxt] = False
            q.append(nxt)
