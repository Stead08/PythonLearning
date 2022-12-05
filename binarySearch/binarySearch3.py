#paiza 博物館に、n 個の財宝が展示されています。各財宝の価値は V_1, V_2, ..., V_n であり、重さは W_1, W_2, ..., W_n です。怪盗であるあなたは、paiza 博物館からちょうど k 個の財宝を盗み出そうとしています。
#k 個の財宝の平均価値を、(k 個の財宝の価値の和) ÷ (k 個の財宝の重さの和) で定義します。
#盗み出す財宝を適切に選んだ結果、平均価値が最大でいくつになるかを答えてください。
n, k = map(int, input().split())
W = [int(x) for x in input().split()]
V = [int(x) for x in input().split()]

left, right = 0, 5001
for _ in range(100):
    mid = (left + right) / 2

    tmp = [0] * n
    for i in range(n):
        tmp[i] = V[i] - W[i] * mid
    tmp.sort(reverse=True)

    if sum(tmp[:k]) >= 0:
        left = mid
    else:
        right = mid

print(left)
