#行列の行数n、列数m
n, m = map(int, input().split())
#求めたい領域の左上(a, b),右下(c, d)
a, b, c, d = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

#累積和の行列を作成
s = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + l[i][j]

print(s[c + 1][d + 1] - s[a][d + 1] - s[c + 1][b] + s[a][b])
