#ハッシュの計算のための数値a, b
a, b = map(int, input().split())
#対象の数値の要素数
q = int(input())
#今回はtableを１００に設定
table = [[] for _ in range(100)]

for _ in range(q):
    s, t = map(int, input().split())
    #s == 1 の時、数値をハッシュテーブルに格納
    if s == 1:
         #任意のハッシュ関数h(t)でハッシュ化
        h = (a * t + b) % 100
        table[h].append(t)
    #s == 2 の時はtがハッシュテーブル内に存在するか判定
    else:
        h = (a * t + b) % 100
        if t in table[h]:
            print("Yes")
        else:
            print("No")
#ハッシュテーブルを出力
for i in table:
    print(*i)
