# 頂点 X から深さ優先探索をしたときに訪れる頂点の番号を順に改行区切りで出力
import sys
sys.setrecursionlimit(10 ** 6)
#頂点の数 N と辺の本数 M, 頂点番号 X 
n, m, x = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

for i in range(n):
    g[i].sort()
visited = [False] * n    

x -= 1

def dfs(x):
    visited[x] = True
    print(x+1)
    for i in range(len(g[x])):
        if visited[g[x][i]] == False:
            dfs(g[x][i])
dfs(x)
