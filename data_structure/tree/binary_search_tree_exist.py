from collections import defaultdict
# 二分探索木の頂点の数 N, 与えられる数の個数 K, 二分探索木の根の値 R 
n, k, r = map(int, input().split())

binary_tree = [-1] * 1000000
location = defaultdict(int)

location[r] = 0
binary_tree[0] = r

for _ in range(n - 1):
    a, b = map(int, input().split())
    if b < a:
        location[b] = 2 * location[a] + 1
    else:
        location[b] = 2 * location[a] + 2
    
    binary_tree[location[b]] = b

for _ in range(k):
    now = 0
    q = int(input())
    
    while binary_tree[now] != -1:
        if q == binary_tree[now]:
            print("Yes")
            break
        if q < binary_tree[now]:
            now = 2 * now + 1
        else:
            now = 2 * now + 2
        
    if binary_tree[now] == -1:
        print("No")
