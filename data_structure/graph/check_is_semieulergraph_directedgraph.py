'''
弱連結な有向グラフにおいて、すべての辺を一筆書きすることができるための必要十分条件

・すべての頂点において、入次数と出次数が一致する。
　
or 

・以下の条件をすべて満たす。

・(入次数) = (出次数 + 1) となる頂点がちょうど 1 つ存在する。

・(入次数 + 1) = (出次数) となる頂点がちょうど 1 つ存在する。

・残りのすべての頂点について、入次数と出次数が一致する。
'''
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

in_equal_out_plus1 = 0
inplus1_equal_out = 0
else_count = 0
is_semi_Eulergraph = False
for i in range(n):
    if g_in_count[i] == g_out_count[i] + 1:
        in_equal_out_plus1 += 1
    elif g_in_count[i] + 1 == g_out_count[i]:
        inplus1_equal_out += 1
    elif g_in_count[i] == g_out_count[i]:
        else_count += 1
else:
    if in_equal_out_plus1 == 1 and inplus1_equal_out == 1 and else_count == n - 2:
        is_semi_Eulergraph = True
    elif in_equal_out_plus1 == 0 and inplus1_equal_out == 0 and else_count == n:
        is_semi_Eulergraph = True
if is_semi_Eulergraph == True:
    print(1)
else:
    print(0)
