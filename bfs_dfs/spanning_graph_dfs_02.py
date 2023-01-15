# https://paiza.jp/works/mondai/graph_dfs_problems/graph_dfs__tree_step3
# 隣接リストと枝集合 E 
#このとき、この隣接リストから E に含まれない枝を n-1 個選んで全域木を構成し、出力
#E の枝を使わなければ全域木を構成できない場合は -1 と出力

n = int(input())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))
    
k = int(input())
for i in range(k):
    e, d = map(int, input().split())
    ad_list[e].remove(d)
    ad_list[d].remove(e)
    
tree = []

def dfs(v, visited):
    for i in ad_list[v]:
        if i not in visited:
            visited.append(i)
            tree.append((v, i))
            dfs(i, visited)
            
dfs(1, [1])
if len(tree) == n - 1:
    for e in tree:
        print(*e)
else:
    print(-1)
