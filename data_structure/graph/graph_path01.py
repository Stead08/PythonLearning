import random 
#頂点数nの完全グラフで、頂点 s から k 回移動する経路（パス）をどれか 1 つ出力
#n, s, k = 3, 1, 2
n, s, k = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    a = list(range(1, n+ 1))
    a.remove(i)
    ad_list[i] = a
# ad_list = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
path = [s]

for _ in range(k):
    #訪問済みの頂点をpathに追加して、行ける頂点集合と訪問ずみ集合で差集合をとる
    next_s = list(set(ad_list) - set(path))
    s = random.choice(next_s)
    path.append(s)
print(*path)
