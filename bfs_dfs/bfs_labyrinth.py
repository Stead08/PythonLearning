from collections import deque
#マップの行数H,列数w,探索回数n
H, W, = map(int, input().split())
#スタート地点
y, x = map(int, input().split())
#ゴール地点
gy, gx = map(int, input().split())
#que作成
q = deque()
#スタート位置を入れる
q.append((y, x))
#各マスの移動回数を記録するためのリストを作成
l = [[-1] * W for _ in range(H)]
#スタート地点は0回移動
l[y][x] = 0
#マップを入力
mp = []
for _ in range(H):
    s = list(input())
    mp.append(s)
mp[y][x] = "*"
#bfs
while q:
    #queからFIFOで一つ取り出す
    ny, nx = q.popleft()
    #前後左右の探索
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        #もし上下左右で移動可能だったら
        if 0 <= ny + dy < H and 0 <= nx + dx < W and mp[ny + dy][nx + dx] != "#":
            #候補がまだ移動したことがない座標だったら
            if l[ny + dy][nx + dx] == -1:
                #移動元が既に何回移動してきたかがl[ny][nx]でそれに一回追加したものを移動先座標のlに代入
                l[ny + dy][nx + dx] = l[ny][nx] + 1
                #移動したのでそれを示すために"*"にする
                mp[ny + dy][nx + dx] = "*"
                #移動先をqueに入れる
                q.append((ny + dy, nx + dx))
#ゴール判定
if mp[gy][gx] == "*":
    #ゴールまで最短何歩移動するか
    print(l[gy][gx])
else:
    print("No")
    
