#最小値の最大化問題
#https://paiza.jp/works/mondai/binary_search/binary_search__application_step2
#L:長さ, n:分ける人数, k:切れ目の数
L, n, k = map(int, input().split())
A = [int(x) for x in input().split()]

A = [0] + A + [L]
left, right = 0, L + 1
#長さ mid 以上の太巻きの本数を最大化
while right - left > 1:
    #最も短い太巻きがmid(cm)の時
    mid = (left + right) // 2

    last_index, parts = 0, 0
    for i in range(k + 2):
        #あるのは切れ目であって切れているわけではないのでどこの切れ目を選んだらmid(cm)切れるか探す。
        #i番目の切れ目まででmid(cm)切れるか
        if A[i] - A[last_index] >= mid:
            #もしできる場合切り取る
            parts += 1
            #切り取ったので切り取った切れ目から探索する
            last_index = i
    #n本必要なのにn本できなかった場合
    if parts < n:
        #上限をmidにして再探索
        right = mid
    else:
        left = mid

print(left)
