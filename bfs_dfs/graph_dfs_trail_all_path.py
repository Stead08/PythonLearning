#頂点 s から k 回移動する経路（トレイル）を全て出力
#トレイルとは枝の反復を許さず頂点の反復を許す経路

n, s, k = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

path = []
edges = []
def dfs(v, trail, edges, k):
    if k == 0:
        path.append(tuple(trail))
    else:
        for i in ad_list[v]:
            e = sorted((i, v))
            if e not in edges:
                trail.append(i)
                edges.append(e)
                dfs(i, trail, edges, k - 1)
                trail.pop()
                edges.pop()

dfs(s, [s], [], k)
#------------------------
print(len(path))
for i in path:
    print(*i)
