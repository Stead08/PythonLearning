from collections import defaultdict

N, R = map(int, input().split())

location = defaultdict(int)
binary_tree = [-1] * 1000000

location[R] = 0
binary_tree[0] = R

for _ in range(N - 1):
    a, b, LR = input().split()
    a = int(a)
    b = int(b)
    is_binary_search_tree = True
    if LR == "L":
        location[b] = 2 * location[a] + 1
        if a <= b:
            is_binary_search_tree = False
    else:
        location[b] = 2 * location[a] + 2
        if b <= a:
            is_binary_search_tree = False

    if binary_tree[location[b]] != -1 or not is_binary_search_tree:
        print("NO")
        exit()
    else:
        binary_tree[location[b]] = b

print("YES")
