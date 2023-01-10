#https://atcoder.jp/contests/abc213/tasks/abc213_d
#再帰回数上限
import sys
sys.setrecursionlimit(10**6)

# 入力の受け取り
n = int(input())

# 道の情報格納リスト
connect = [[] for i in range(n + 1)]

# 道の情報受け取り
for i in range(n-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

# 頂点番号が小さい順から回るのでソート
for i in range(n + 1):
    connect[i].sort()

ans = []

# DFS（今いる町, 前にいた町)
def dfs(now, prev):
    # 今いる町を答えに入れる
    ans.append(now)
    # to = 今いる町から行ける町
    for to in connect[now]:
        # もしtoが前にいた町と違うなら
        if to != prev:
            dfs(to, now)
            # 戻ってきたらansへ格納
            ans.append(now)

# 最初の町=1,前にいた町=-1(前にいた町がないので便宜上-1)としてスタート
dfs(1,-1)

# 答えの出力
print(*ans)