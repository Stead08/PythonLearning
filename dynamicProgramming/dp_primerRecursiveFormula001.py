#二項間漸化式
#初項x, 交差dのk項目の値を求める
x, d, k = map(int, input().split())
A = [x] * (k + 1)
for i in range(2, k + 1):
    A[i] = A[i-1] + d

print(A[k])
