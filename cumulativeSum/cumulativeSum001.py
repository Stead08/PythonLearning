#https://paiza.jp/works/mondai/prefix_sum_problems/prefix_sum_problems__section_sum_step3
# 行目に整数 X, Y が与えられます。
#2 行目に 10 個の整数 a_0, a_1, a_2, ..., a_9 からなる数列 a を入力
#この数列の a_X から a_Y までの和 (a_X + a_{X + 1} + ... + a_Y) を、累積和を使うことで求め、一行で出力

x, y = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
for i in A:
    s = i + S[-1]
    S.append(s)
print(S[y + 1]-S[x])
