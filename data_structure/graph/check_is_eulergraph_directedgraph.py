#弱連結な有向グラフにおいて、ある頂点から始めてすべての辺を一筆書きして最初の頂点に戻ってくることができるための必要十分条件:
#すべての頂点において、入次数と出次数が一致する。
n, m = map(int, input().split())
g_out = [[] for _ in range(n)]
g_in = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g_in[a].append(b)
    g_out[b].append(a)
g_in_count = []
g_out_count = []
for i in g_in:
    g_in_count.append(len(i))
for i in g_out:
    g_out_count.append(len(i))
#入次数と出次数が一致しているかチェック
for i in range(n):
    if g_in_count[i] != g_out_count[i]:
        print(0)
        break
else:
    print(1)
