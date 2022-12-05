#長さkのフィボナッチ数列の最後の値を求める
k = int(input())
A = [1, 1]
for i in range(k - 2):
    A.append(A[-2] + A[-1])
print(A[-1])
