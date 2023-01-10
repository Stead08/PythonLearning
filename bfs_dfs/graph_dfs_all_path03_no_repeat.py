#頂点 s と頂点 t を端点とするパスを全て出力
#　頂点と枝の反復を許さない経路
n, s, t = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

paths = []

def dfs(v, path):
    for i in ad_list[v]:
        if i not in path:
            path.append(i)
            if i == t:
                paths.append(tuple(path))
            else:
                dfs(i, path)
            path.pop()


dfs(s, [s])

print(len(paths))
for i in paths:
    print(*i)
