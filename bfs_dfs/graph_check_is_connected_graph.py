n = int(input())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))


def dfs(v, visited):
    if len(visited) == n:
        print("Yes")
        exit()
    else:
        for i in ad_list[v]:
            if i not in visited:
                visited.append(i)
                dfs(i, visited)


dfs(1, [1])
print("No")
