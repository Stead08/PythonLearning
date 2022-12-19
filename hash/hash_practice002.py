#オープンアドレス法を用いてハッシュテーブルを実装
table = [-1] * 10

n = int(input())

for i in range(n):
    x = int(input())
#hashを初期値で計算
    hash = x % 10
#hash値が被ってたら再計算、かぶらなくなるまでループ
    while table[hash] != -1:
        hash = (hash + 1) % 10

    table[hash] = x

for i in range(10):
    print(table[i])
