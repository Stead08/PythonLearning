# 頂点 s と頂点 t を端点とするトレイルのうち、s と t どちらの頂点も通過点としても含む(s と t のどちらもトレイルに 2 回以上含まれる）ものを全て出力
n, s, t = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

trails = []


def dfs(v, trail, edges):
    for i in ad_list[v]:
        e = sorted((i, v))
        if e not in edges:
            trail.append(i)
            edges.append(e)
            if i == t:
                if trail.count(s) >= 2 and trail.count(t) >= 2:
                    trails.append(tuple(trail))
            dfs(i, trail, edges)
            edges.pop()
            trail.pop()


dfs(s, [s], [])

print(len(trails))
for i in trails:
    print(*i)
