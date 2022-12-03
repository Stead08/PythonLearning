#https://paiza.jp/works/mondai/prefix_sum_problems/prefix_sum_problems__sum_max_boss
#【連続する N 個の和の最大値】 連続する N 個の和の最大値
#1 行目に整数 N, K が与えられます。
#2 行目に N 個の整数 a_0, a_1, a_2, ..., a_(N-1) が与えられます。
#連続する K 個の整数の和の最大値を、累積和を使うことで求め、一行で出力してください。

n, k = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
#累積和の数列を作成
for i in A:
    s = i + S[-1]
    S.append(s)
l = []

for i in range(n - k + 1):
    l.append(S[i+k] - S[i])
print(max(l))
