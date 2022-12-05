# a_1 = x 
# a_n = a_{n-1} + d_1 (n が奇数のとき、n ≧ 3) 
# a_n = a_{n-1} + d_2 (n が偶数のとき)
# 数列の k 項目の値を出力
#初項x,　奇数の時の公差d_1, 偶数の場合d_2, 数列の長さk
x, d_1, d_2, k = map(int, input().split())
a = [x] * (k + 1)
for i in range(2, k + 1):
    if i % 2 == 0:
        a[i] = a[i - 1] + d_2
    elif i % 2 == 1:
        a[i] = a[i - 1] + d_1
print(a[k])
