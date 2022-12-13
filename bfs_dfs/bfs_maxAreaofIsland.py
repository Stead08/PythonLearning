#1（陸）と0（水）の地図を表すm×nの2次元二項格子が与えられたとき、最大面積の島の面積を返す。
#島は水に囲まれ、隣接する陸地が水平または垂直に結ばれて形成される。グリッドの4つの辺はすべて水に囲まれていると考えてよい。
#https://leetcode.com/problems/number-of-islands/
from collections import deque
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]



def maxAreaofIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    max_area = 0
    #map全体の高さと広さを取得（rows = 行, cols =列
    rows, cols = len(grid), len(grid[0])
    #既に探索済みなところを集合で記録する
    visited = set()
    #島の数を数えるので0で初期化
    count = 0
    #幅優先探索
    def bfs(r, c):
        q = deque()
        area = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q.append((r, c))
        while q:
            row, col = q.popleft() #popleftをpopに変えると深さ優先探索
            for dir_r, dir_c in directions:
                adj_r, adj_c = row + dir_r, col + dir_c
                if (adj_r in range(rows)
                and adj_c in range(cols)
                and grid[adj_r][adj_c] == "1"
                and (adj_r, adj_c) not in visited):
                    q.append((adj_r, adj_c))
                    visited.add((adj_r, adj_c))
                    area += 1
        return area


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                max_area = max(max_area, bfs(r, c))
    return max_area

print(maxAreaofIslands(grid))
