#n 本のパイプから k 本のパイプを適切に切り出した結果、切り出すことができるパイプの長さの最大値
n, k = map(int, input().split())
A = list(map(int, input().split()))

left, right = 0, 10001
for _ in range(100):
    mid = (left + right) / 2
    num_of_pipes = 0
    for a in A:
        num_of_pipes += a // mid

    if num_of_pipes < k:
        right = mid
    else:
        left = mid

print(left)
