#頂点 s と t を端点とするトレイルのうち最も頂点数の多いものを求める
# トレイルとは枝の反復を許さず頂点の反復を許す経路

n, s, t = map(int, input().split())
ad_list = {}
for i in range(1, n+1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

max_trail = ()
def dfs(v, trail, edges):
    for i in ad_list[v]:
        e = sorted((i, v))
        if e not in edges:
            trail.append(i)
            if i != s:
                edges.append(e)
                if i == t:
                    global max_trail
                    if len(max_trail) < len(trail):
                        max_trail = tuple(trail)
                else:
                    dfs(i, trail, edges)
                edges.pop()
            trail.pop()

dfs(s, [s], [])

print(*max_trail)
