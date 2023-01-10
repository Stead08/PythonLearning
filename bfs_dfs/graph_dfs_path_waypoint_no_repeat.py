# 経路での反復が許されない深さ優先探索, pを経由するという条件つき
#　経路全出力
n, s, t, p = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))
    
#ad_list = {1: [2, 5], 2: [1, 3, 5], 3: [2, 4, 5], 4: [3, 5], 5: [1, 2, 3, 4]}
paths = []
def dfs(v, path):
    if v == t and p in path:
        paths.append(tuple(path))
    else:
        for i in ad_list[v]:
            if i not in path:
                path.append(i)
                dfs(i, path)
                path.pop()


dfs(s, [s])
#-----ans--------
# path数出力
print(len(paths))
for i in paths:
    print(*i)
