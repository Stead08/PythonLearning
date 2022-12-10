#数列の連続した要素の和の最大値をしゃくとり法を用いて求める。
#数列の長さn、区間の長さ
n, x = map(int, input().split())
#数列の入力
l = list(map(int, input().split()))
#dpじゃない気がするが区間和を記録するリストを作成
dp = [0] * (n)
#最初の区間和を計算
dp[0] = sum(l[0:x])
#しゃくとり法で区間和を求めていく
for i in range(1, n - x + 1):
  #一個前の区間和とあたらしい区間和のかぶってないところを引いたり足したりする．
    dp[i] = dp[i-1] - l[i-1] + l[i + x - 1] 
#もとまった区間和の最大値を求める
max_index = dp.index(max(dp))
#最大値と最大値が現れる最初の区間和を構成する最初の要素を出力
print(max(dp), l[max_index])
