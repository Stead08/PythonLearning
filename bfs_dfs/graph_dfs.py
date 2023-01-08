# 頂点 X から深さ優先探索をしたときに訪れる頂点の番号を順に改行区切りで出力
import sys
sys.setrecursionlimit(10 ** 6)
#頂点の数 N と辺の本数 M, 頂点番号 X 

def dfs(now: int):
    unvisited[now] = False
    print(now + 1)
    for i in range(len(graph[now])):
        if unvisited[graph[now][i]]:
            dfs(graph[now][i])


N, M, X = map(int, input().split())
X -= 1

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    graph[i].sort()

unvisited = [True] * N
dfs(X)
