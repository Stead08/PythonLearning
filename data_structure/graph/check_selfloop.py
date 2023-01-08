#与えられた隣接行列から自己ループの数と頂点番号を出力
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

vertex_l = []
# 自己ループ辺はg[i][i] == 1で判定できる
for i in range(n):
    if g[i][i] == 1: 
        vertex_l.append(i)
print(len(vertex_l))
for i in vertex_l:
    print(i+1)
