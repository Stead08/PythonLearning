#n:頂点数, s: start, t:target
# 存在しない場合は-1を出力
n, s, t = map(int, input().split())
k = int(input())
# 通らない頂点の集合
S = list(map(int, input().split()))
S = set(S)
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))
    
min_path = tuple(range(1, n + 2))
def dfs(v, path):
    global min_path
    if len(path) < len(min_path):
        #「訪問済みの頂点の配列の長さ」が「暫定で頂点数が最も少ないパスの長さ」よりも短い場合で操作を行うことで計算時間減少
        for i in ad_list[v]:
            if i not in path:
                path.append(i)
                #pathとSが互いに素である場合
                if i == t and S.isdisjoint(set(path)) == True:
                    min_path = tuple(path)
                else:
                    dfs(i, path)
                path.pop()

dfs(s, [s])

if min_path[0] == s and min_path[-1] == t:
    print(*min_path)
else:
    print(-1)
