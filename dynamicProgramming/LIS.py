#最長増加部分列,Longest Increasing Subsequence
#数列の長さn
n = int(input())
#数列a
a = []
for _ in range(n):
    a.append(int(input()))
#数列の最終要素の最小値は1で初期化
dp = [1] * n
#増加部分列の長さiでfor loop
for i in range(1, n):
    for j in range(0, i):
        if a[j] <= a[i]: #作った増加部分列の数列の最終要素がが今までの中で最小値だった場合更新
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
