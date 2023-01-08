# 多重辺・有向グラフ (辺入力)
# https://paiza.jp/works/mondai/graph_input_problems/graph_input_problems__loops_multiple_edges_boss
from collections import defaultdict
n, m = map(int, input().split())

edges = defaultdict(int)
multipleEdges = []
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    
    edges[(a, b)] += 1

for key, value in edges.items():
    if value > 1:
        multipleEdges.append(key)

print(len(multipleEdges))
for i in sorted(multipleEdges):
    print(*i)
