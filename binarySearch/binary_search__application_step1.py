#平均最大化問題
#https://paiza.jp/works/mondai/reviews/show/ca9d987d8f775f45855f98ef7524377d
#Wからk個選んで、そのkらの(Vの平均/Wの平均)を最大化する
#x = kらの(Vの平均/Wの平均)とする
n, k = map(int, input().split())
W = [int(x) for x in input().split()] #価値
V = [int(x) for x in input().split()]　#重さ
#xの上限を5000と仮定
#ここからのコメントは一周目どうなってるかのメモ
left, right = 0, 5001
for _ in range(100):
    mid = (left + right) / 2
    #中央の2500を達成できる組み合わせはあるか？
    #xの候補リストを0で初期化
    tmp = [0] * n
    
    for i in range(n):
        #平均価値が mid 以上になるためには
        #(v_1 + v_2 + ... + v_k) / (w_1 + w_2 + ... + w_k) ≧ mid
        #同値変形して(v_1 + v_2 + ... + v_k) - mid * (w_1 + w_2 + ... + w_k) ≧ 0
        #tmp[i]は左辺の値を調べている（ただしk = nとして効率化（どれを選んだかは答えに必要がないため）
        tmp[i] = V[i] - W[i] * mid
    tmp.sort(reverse=True)
    #tmpを大きい方を先頭にしてソート
    if sum(tmp[:k]) >= 0:
        #kばんめまでのtmpのsum(つまり価値midでの最大の価値）が0より大きいか。そうでなければ入力のWとVではmidは達成できない。できた場合より大きいmidで達成できるか探索
        left = mid
    else:
        right = mid

print(left)
