# グラフの閉路の総数

n, s = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))
c = 0
def dfs(v, visited):
    for i in ad_list[v]:
        if i == s and len(visited) > 2:
            visited.append(i)
            global c
            c += 1
            visited.pop()
        elif i not in visited:
            visited.append(i)
            dfs(i, visited)
            visited.pop()
dfs(s, [s])
print(c // 2)
