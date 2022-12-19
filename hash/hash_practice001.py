#名前と番号をハッシュテーブルに格納するInput部分と,　入力された名前に応じた番号を出力するoutput部分で構成される。
#ハッシュの最大値を定義
HASH = 5
#名前を格納する配列を用意
name = [None] * HASH
#番号を格納する配列を用意
tel = [None] * HASH
#ハッシュ関数の定義
def hash(key):
    h = 0
    for i in key:
        h += ord(i)
    return h%HASH
#------------------------------------
while True:
    n = input("名前を入力してください")
    if n == "":
        break
    t = input("番号を入力してください")
    h = hash(n)
    #ハッシュ値に対応するリストの場所に名前を格納
    name[h] = n
    #同様に番号を格納
    tel[h] = t
    print("ハッシュ値", h, "データ格納完了")

print(name)
print(tel)

while True:
    n = input("検索する名前は？")
    if n == "":
        break
    h = hash(n)
    if name [h] == n:
        print(n + "さんの番号は" + tel[h])
    else:
        print("その名前は登録されていません。")
