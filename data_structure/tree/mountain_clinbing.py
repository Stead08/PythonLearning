def calc_length(now: int):
    for nxt in g[now]:
        if len_from_T[nxt] == -1:
            len_from_T[nxt] = len_from_T[now] + 1
            parent[nxt] = now
            calc_length(nxt)
# 山のチェックポイントの数 N, 
# 山の頂点に割り当てられたチェックポイントの番号 T,
# paiza 君が出発したチェックポイントの番号 S,
# paiza 君が山を登った回数 C, 降りた回数 D
n, t, s, c, d = map(int, input().split())

g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

parent = [0] * n
#頂点なので親なし
parent[t - 1] = -1
len_from_T = [-1] * n
#頂点から頂点の距離は０
len_from_T[t-1] = 0

calc_length(t-1)

if len_from_T[s-1] <= c:
    for i in range(n):
        if len_from_T[i] == len_from_T[s-1] - c + d:
            print(i + 1)
else:
    highest = s - 1
    for i in range(c):
        highest = parent[highest]
    
    for i in range(n):
        if len_from_T[i] == len_from_T[s - 1] - c + d:
            ancestor = i
            for j in range(d):
                ancestor = parent[ancestor]
            
            if ancestor == highest:
                print(i + 1)
