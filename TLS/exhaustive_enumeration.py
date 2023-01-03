#　標準入力
#n　座標の数
#x_1 y_1
#x_2 y_2
#...
#x_n y_n
# 順列全列挙でTSPの厳密解を求める
import itertools
from math import sqrt

def distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
n = int(input())
coodinates = [list(map(int, input().split())) for _ in range(n)]
ans_l = []
point_num = list(range(1, n+1))
for route in itertools.permutations(point_num):
    ans_dis = 0
    for i in range(len(route) - 1):
        ans_dis += distance(coodinates[route[i] - 1], coodinates[route[i+1] - 1])
    ans_dis += distance(coodinates[route[0]-1], coodinates[route[-1] - 1])
    ans_l.append((ans_dis, route))

ans = min(ans_l)
print(ans[0])
print(*ans[1])
