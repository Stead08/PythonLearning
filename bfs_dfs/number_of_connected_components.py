import sys 

sys.setrecursionlimit(10 ** 6)

def dfs(now: int, num: int):
    color[now] = num
    for i in range(len(graph[now])):
        if color[graph[now][i]] == -1:
            dfs(graph[now][i], num)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

ans = 0

color = [-1] * n
for i in range(n):
    if color[i] == -1:
        dfs(i, ans)
        ans += 1

print(ans)
