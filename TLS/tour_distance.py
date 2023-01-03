#巡回路長の計算
from math import sqrt
def distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

n = int(input())
#座標の入力
l = []
for _ in range(n):
    x, y = map(int, input().split())
    l.append((x, y))
#ルートの入力
route = list(map(int, input().split()))
ans_dis = 0
#ルートに沿って距離を積算していく
for i in range(len(route) - 1):
    ans_dis += distance(l[route[i] - 1], l[route[i+1] - 1])

ans_dis += distance(l[route[0]-1], l[route[-1] - 1])
print(ans_dis)
