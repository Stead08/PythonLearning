# 根付き木の頂点の数 N, 与えられる頂点の数 K, 二分木の根の頂点番号 R
n, k, r = map(int, input().split())
# 各頂点について構造体を作成（[0] はL、[1]はRとする
g = [[-1, -1] for _ in range(n)]
#　二分木の入力
for _ in range(n - 1):
    a, b, lr = input().split()
    a = int(a) - 1
    b = int(b) - 1
    if lr == "L":
        g[a][0] = b
    elif lr == "R":
        g[a][1] = b
# 標準入力で入力される各頂点と左右の情報から指定されたこの頂点番号を出力
for _ in range(k):
    v, lr = input().split()
    v = int(v) - 1
    if lr == "L":
        if g[v][0] != -1:
            print(g[v][0] + 1)
        else:
            print()
    if lr == "R":
        if g[v][1] != -1:
            print(g[v][1] + 1)
        else:
            print()
