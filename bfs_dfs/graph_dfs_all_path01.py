# path深さ優先探索全列挙
n, s, k = map(int, input().split())
ad_list = {}
for i in range(1, n + 1):
    v = int(input())
    ad_list[i] = list(map(int, input().split()))
    
#ad_list = {1: [2, 5], 2: [1, 3, 5], 3: [2, 4, 5], 4: [3, 5], 5: [1, 2, 3, 4]}
path = []
def dfs(v:int, walk:list, k:int):
    if k == 0:
        path.append(tuple(walk))
    else:
        for i in ad_list[v]:
            walk.append(i)
            dfs(i, walk, k-1)
            walk.pop()


dfs(s, [s], k)
print(len(path))
for i in path:
    print(*i)

