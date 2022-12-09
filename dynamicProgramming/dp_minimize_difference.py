#リスト内の各数値の差の最小値は何かを動的計画法で求める（このコードで合ってるのか未確認）
#データ量が膨大な場合、ソートも効率化しないといけない
#二部探索でこういう問題解けるのか気になる
n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()
dp = [0] * n
dp[0] = l[1] - l[0]
for i in range(1, n):
    s = l[i] - l[i-1]
    dp[i] = min(dp[i-1], s)

print(dp[n-1])
