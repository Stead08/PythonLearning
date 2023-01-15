n, e1, e2 = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))


def dfs(v, visited):
    for i in ad_list[v]:
        if i == e1 and len(visited) > 2:
            visited.append(i)
            print(*visited)
            exit()
        elif i not in visited:
            visited.append(i)
            dfs(i, visited)
            visited.pop()


dfs(e2, [e1, e2])

print(-1)
