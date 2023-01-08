# 深さ優先探索で３マス移動した後にいるマスの座標を出力
h, w, y, x = map(int, input().split())

def dfs(times: int, y: int, x: int):
    if times == 3:
        print(y, x)
    else:
      # 探索の際の移動は上,右,下,左の順におこなうものとし、グリッドの左上・右上・左下・右下のマスをそれぞれ (0,0), (0,W-1), (H-1,0), (H-1,W-1)とする
        if 0 <= y - 1:
            dfs(times + 1, y - 1, x)
        if x + 1 < w:
            dfs(times + 1, y, x + 1)
        if y + 1 < h:
            dfs(times + 1, y + 1, x)
        if 0 <= x - 1:
            dfs(times + 1, y, x - 1)

dfs(0, y, x)
