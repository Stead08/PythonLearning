#頂点 s から k 回移動する経路（トレイル）をどれか 1 つ出力
#トレイルとは枝の反復を許さず頂点の反復を許す経路

n, s, k = map(int, input().split())
import random

edges = []

trail = [s]
for _ in range(k):
    ng_neibours = set()
    while True:
        next_s = random.choice(list(set(range(1, n + 1)) - {s} - ng_neibours))
        e = tuple(sorted((s, next_s)))
        if e not in edges:
            break
        ng_neibours.add(next_s)
    trail.append(next_s)
    edges.append(e)
    s = next_s

print(*trail)
