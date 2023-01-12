#pを二回以上経由するトレイルを全出力

n, s, t, p = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

path = []
edges = []
def dfs(v, trail, edges):
    for i in ad_list[v]:
        e = sorted((i, v))
        if e not in edges:
            trail.append(i)
            edges.append(e)
            if i == t and trail.count(p) >= 2:
                path.append(tuple(trail))
            else:
                dfs(i, trail, edges)
            edges.pop()
            trail.pop()

dfs(s, [s], [])
#------------------------
print(len(path))
for i in path:
    print(*i)
