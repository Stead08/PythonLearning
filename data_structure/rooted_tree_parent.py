#根付き木の頂点の数 N, 与えられる頂点の数 K, 根付き木の根の頂点番号 R 
n, k, r = map(int, input().split())

# 各頂点について構造体を作成し、その構造体の中に子の頂点番号を保持する。
#構造体の中にさまざまな値を持たせることができるので拡張性があるのでこの方法を使うのが良い。
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a-1].append(b)

for i in range(n):
    g[i].sort()

for _ in range(k):
    v = int(input())
    print(*g[v-1])
