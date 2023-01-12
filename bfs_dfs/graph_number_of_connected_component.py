n = int(input())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))

def dfs(v, connected_comp):
    for i in ad_list[v]:
        if i not in connected_comp:
            connected_comp.append(i)
            dfs(i, connected_comp)
    return connected_comp

count = 0
unvisited = set(range(1, n + 1))
while len(unvisited) > 0:
    v = unvisited.pop()
    unvisited -= set(dfs(v, [v]))
    count += 1
print(count)
