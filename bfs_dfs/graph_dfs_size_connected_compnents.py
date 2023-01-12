# グラフの各連結成分の頂点数が k 以下なら Yes を出力し、そうでなければ No を出力
n, k = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

def dfs(v, connected_comp):
    for i in ad_list[v]:
        if i not in connected_comp:
            connected_comp.append(i)
            dfs(i, connected_comp)
    return connected_comp, len(connected_comp)

unvisited = set(range(1, n + 1))
while len(unvisited) > 0:
    v = unvisited.pop()
    s = dfs(v, [v])
    unvisited -= set(s[0])
    if s[1] > k:
        print("No")
        break
else:
    print("Yes")
