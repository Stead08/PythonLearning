# 全域木か判定する
n = int(input())
ad_list = {}
edge_num = 0
for i in range(1, n + 1):
    v = int(input())
    edge_num += v
    ad_list[i] = list(map(int, input().split()))
    
def dfs(v, visited):
    for i in ad_list[v]:
        if i not in visited:
            visited.append(i)
            dfs(i, visited)
    return visited

if edge_num // 2 > n - 1:
    print("No")
else:
    if len(dfs(1, [1])) == n:
        print("Yes")
    else:
        print("No")
