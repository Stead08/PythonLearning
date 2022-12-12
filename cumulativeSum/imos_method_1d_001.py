#https://paiza.jp/works/mondai/prefix_sum_problems/prefix_sum_problems__1d_imos_boss
#1 次元上のいもす法
#ますの数n, 加算処理をする範囲の数q
n, q = map(int, input().split())
L = []
R = []
a = [0] * (n + 1)
#開始地点をLに、終了時点+ 1ますをRに
for _ in range(q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
#数列に適用（開始地点+=1, 終了時点-=1)
for i in range(q):
    a[L[i] - 1] += 1
    a[R[i]] -= 1
#累積和をとる
for i in range(n):
    a[i+1] += a[i]
print(max(a))
