n, k, r = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = input().split()
    a = int(a) - 1
    b = int(b) - 1
    g[a].append(b)


for _ in range(k):
    v, k = input().split()
    v = int(v) - 1
    k = int(k) - 1
    print(g[v][k] + 1)
