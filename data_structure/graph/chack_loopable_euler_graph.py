#オイラーグラフは簡単に説明すると一筆書きができるグラフ
# オイラーグラフ成立の必要十分条件は全ての頂点の次数が偶数であることである。
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

#　オイラーグラフであれば１、そうでなければ０を出力
for i in g:
    if len(i) % 2 == 1:
        print(0)
        break
else:
    print(1)
