# ~ n の番号がついた n 個のおもりがあり、おもり i の重さは a_i です。
# おもりを何個か選んで重さの和が x となるようにすることができるかどうか判定してください。

n, x = map(int, input().split())
a = [int(input()) for i in range(n)]

dp = [False] * (x + 1)
dp[0] = True

for val in a:
    for j in range(x, val - 1, -1):
        if dp[j - val]:
            dp[j] = True

if dp[x]:
    print("yes")
else:
    print("no")
