#n:頂点数, s: start, t: target
# 頂点 s と頂点 t を端点とするパスでpを経由するもののうち、頂点数が最も少ないものを 1 つ出力
# 存在しない場合は-1を出力
n, s, t, p = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))
    
#ad_list = {1: [2, 5], 2: [1, 3, 5], 3: [2, 4, 5], 4: [3, 5], 5: [1, 2, 3, 4]}
min_path = tuple(range(1, n + 2))
def dfs(v, path):
    global min_path
    if len(path) < len(min_path):
        #「訪問済みの頂点の配列の長さ」が「暫定で頂点数が最も少ないパスの長さ」よりも短い場合で操作を行うことで計算時間減少
        for i in ad_list[v]:
            if i not in path:
                path.append(i)
                if i == t and p in path:
                    min_path = tuple(path)
                else:
                    dfs(i, path)
                path.pop()

dfs(s, [s])

if min_path[0] == s and min_path[-1] == t:
    print(*min_path)
else:
    print(-1)
