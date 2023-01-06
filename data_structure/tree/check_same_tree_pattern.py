from itertools import permutations
from collections import defaultdict
# 実際に V_1 と V_2 の頂点の対応を全探索することができれば、その中に辺集合が一致するものがあった場合は YES , ない場合は NO 
N_1 = int(input())
g_1 = [[] for _ in range(N_1)]
for _ in range(N_1 - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g_1[a].append(b)
    g_1[b].append(a)

N_2 = int(input())
g_2 = [[] for _ in range(N_2)]
for _ in range(N_2 - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g_2[a].append(b)
    g_2[b].append(a)

if N_1 != N_2:
    print("NO")
else:
    for permutation in permutations(range(N_1)):
        d = defaultdict(int)
        for i, j in enumerate(permutation):
            d[j] = i

        check = True
        for i in range(N_1):
            if len(g_1[i]) != len(g_2[d[i]]):
                check = False
        if check:
            print("YES")
            break
    else:
        print("NO")
