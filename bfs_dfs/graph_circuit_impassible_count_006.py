n, t = map(int, input().split())

#通れない頂点群
k = int(input())
S = set(map(int, input().split()))
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))
#隣接リストから通れない頂点を削除
for i in S:
    for j in ad_list[i]:
        ad_list[j].remove(i)
    ad_list[i].clear()

c = 0


def dfs(v, visited):
    for i in ad_list[v]:
        if i == t and len(visited) > 2:
            visited.append(i)
            global c
            c += 1
            visited.pop()
        elif i not in visited:
            visited.append(i)
            dfs(i, visited)
            visited.pop()


dfs(t, [t])

print(c // 2)
