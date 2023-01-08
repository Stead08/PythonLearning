#頂点の次数が奇数であるものの数が０または２であれば準オイラーグラフ
# 準オイラーグラフとは一筆書きできるけど最初の頂点に戻る必要がないというオイラーグラフよりも緩い条件で成立するグラフ
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

#　準オイラーグラフであれば１、そうでなければ０を出力
odd_count = 0
for i in g:
    if len(i) % 2 == 1:
       odd_count += 1
if odd_count == 0 or odd_count == 2:
    print(1)
else:
    print(0)
