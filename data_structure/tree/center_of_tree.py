n = int(input())
num_of_vertex = n

# 頂点が木に属するかどうかを管理。iが木に属するときは１、　属さない場合は０
exist = [1] * n
g = [[0] * n for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = 1
    g[b][a] = 1
    
while num_of_vertex > 2:
    for i in range(n):
        cnt = 0
        for j in range(n):
            if g[i][j] == 1:
                cnt += 1
        if cnt == 1:　#葉だった場合　i.g) g[i] = [0, 0, 1, 0, 0]
            num_of_vertex -= 1
            #葉なので木に属さないことにする
            exist[i] = 0
            #木gから葉を削除
            g[i] = [0] * n
    #反対方向で記録されている辺の情報も削除
    for i in range(n):
        for j in range(n):
            if exist[j] == 0 and g[i][j] == 1:
                g[i][j] = 0
# 最後に残っている頂点番号を出力                
for i in range(n):
    if exist[i] == 1:
        print(i+ 1)
