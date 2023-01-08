# 二分グラフ判定
import sys

sys.setrecursionlimit(10 ** 6)

# 色が塗られていない全ての頂点を色 2(1) で塗る。彩色済みの頂点は、その色が 2(1) である場合操作を継続する。1(2) である場合、操作を中断する。
def dfs(now: int, num: int):
    color[now] = num
    for i in range(len(graph[now])):
        if color[graph[now][i]] == 0:
            dfs(graph[now][i], -num)
        else:
            if color[now] == color[graph[now][i]]:
                global ok
                ok = False


N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

ok = True

color = [0] * N
for i in range(N):
    if color[i] == 0:
        dfs(i, 1)

if ok:
    print("Yes")
else:
    print("No")
