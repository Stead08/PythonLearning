#https://paiza.jp/works/mondai/bfs_dfs_problems/bfs_dfs_problems__move_three_times
#指定位置から３マス移動
from collections import deque
#ますの高さと幅
H, W = map(int, input().split())
#開始位置
y, x = map(int, input().split())

q = deque()　#dequeオブジェクトの作成
q.append((y, x))　#queに初期位置を入れる
l = [[-1] * W for _ in range(H)]
l[y][x] = 0
mp = [["."] * W for _ in range(H)]
mp[y][x] = "*"

while q:
    ny, nx = q.popleft()　#queの先頭要素を取り出してqueから削除 pop-left
    if l[ny][nx] == 3: #三回移動済みだったら
        continue　
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):　#今いる位置から上下左右の位置について
        if 0 <= ny + dy < H and 0 <= nx + dx < W:
            if l[ny + dy][nx + dx] == -1:
                l[ny + dy][nx + dx] = l[ny][nx] + 1
                mp[ny + dy][nx + dx] = "*"
                q.append((ny + dy, nx + dx))

for i in range(H):
    print(*mp[i], sep="")
