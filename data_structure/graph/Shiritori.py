# しりとりの入力単語は全て小文字アルファベット
# 各文字列 s_i を頂点 first(s_i) から頂点 last(s_i) へ向かう辺とみなして、準オイラーグラフかどうかの判定
import string
alphabets = list(string.ascii_lowercase)
n = int(input())
g_out = [[] for _ in range(len(alphabets))]
g_in = [[] for _ in range(len(alphabets))]
for _ in range(n):
    s = input()
    a = alphabets.index(s[0])
    b = alphabets.index(s[-1])
    g_in[b].append(a)
    g_out[a].append(b)

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
for i, v in enumerate(zip(g_in_count, g_out_count)):
    if v[0] == v[1] == 0:
        g_in_count.pop(i)
        g_out_count.pop(i)
for i in range(len(g_in_count)):
    if g_in_count[i] == g_out_count[i] + 1:
        in_equal_out_plus1 += 1
    elif g_in_count[i] + 1 == g_out_count[i]:
        inplus1_equal_out += 1
    elif g_in_count[i] == g_out_count[i]:
        else_count += 1
else:
    #準オイラーグラフか判定
    if in_equal_out_plus1 == 1 and inplus1_equal_out == 1 and else_count == len(g_in_count) - 2:
        is_semi_Eulergraph = True
    elif in_equal_out_plus1 == 0 and inplus1_equal_out == 0 and else_count == len(g_in_count):
        is_semi_Eulergraph = True
if is_semi_Eulergraph == True:
    print(1)
else:
    print(0)
