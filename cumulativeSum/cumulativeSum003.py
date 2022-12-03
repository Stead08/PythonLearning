#https://paiza.jp/works/mondai/prefix_sum_problems/prefix_sum_problems__section_count_boss
#区間内の個数
#1 行目に整数 N, X, Y が与えられます。
#2 行目に N 個の整数 a_0, a_1, a_2, ..., a_(N-1) が与えられます。
#この数列の a_X から a_Y までの偶数の個数を、累積和を使うことで求め、一行で出力
n, x, y = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in A:
    if i % 2 == 0:
        B.append(1)
    else:
        B.append(0)
S = [0]
#累積和の数列を作成
for i in B:
    s = i + S[-1]
    S.append(s)
print(S[y + 1] - S[x])
