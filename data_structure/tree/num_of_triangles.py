N = int(input())

g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

num_of_triangles = 0
for i in range(N):
  #b を中心とする三角形の個数は 「b に接続する頂点からなる、相異なる 2 つの頂点のペアの数」と一致
  #この数は、b に接続する辺の数を E(b) をすると E(b) C 2 = E(b) × (E(b)-1) / 2
    num_of_triangles += len(g[i]) * (len(g[i]) - 1) // 2

if num_of_triangles % 2 == 0:
    print("erik")
else:
    print("paiza")
