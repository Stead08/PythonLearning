# ナップサック問題を解く動的計画法
# 計算量　：O(NW)
# N個の品物の重さと価値をweight[i], value[i]とし、ナップサックに入れられる重さの総和をWとするときに、ナップサックに入れられる価値の総和の最大値を求める。
# アルゴリズム定義
def knapsack():
    dp = [[0 for number in range(0, W+1)] for i in range(0, N+1)]

    for i in range(0, N):
        for w in range(0, W+1):
            if w - weight[i] >= 0:
                dp[i+1][w] = max(dp[i][w], dp[i][w-weight[i]] + value[i])

    print(dp[N][W])

# 入力受取
N, W = map(int, (input().split()))
weight = list(map(int, input().split()))
value = list(map(int, input().split()))

# アルゴリズム実行
knapsack()

# 入力
# 6 10
# 2 1 3 2 1 5
# 3 2 6 1 3 85

# 出力
# 96
