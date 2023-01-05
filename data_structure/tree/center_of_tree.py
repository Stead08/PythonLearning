n = int(input())
num_of_vertex = n

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
        if cnt == 1:
            num_of_vertex -= 1
            exist[i] = 0
            g[i] = [0] * n
    for i in range(n):
        for j in range(n):
            if exist[j] == 0 and g[i][j] == 1:
                g[i][j] = 0
                
for i in range(n):
    if exist[i] == 1:
        print(i+ 1)
