#https://paiza.jp/works/mondai/bfs_dfs_problems/bfs_dfs_problems__three_length
from collections import deque
#頂点の数 N と、頂点番号 X 
N, X = map(int, input().split())
#入力からグラフ（ツリー）を作成
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
#幅優先探索
l = [-1] * N
l[X - 1] = 0
q = deque()
#キューに探索のスタート位置を入れる
q.append(X - 1)
while q:
    prev = q.popleft()
    for nxt in graph[prev]:
        if l[nxt] == -1:
            l[nxt] = l[prev] + 1
            q.append(nxt)
#移動回数３で行くことができる頂点を出力
for i in range(N):
    if l[i] == 3:
        print(i + 1)
