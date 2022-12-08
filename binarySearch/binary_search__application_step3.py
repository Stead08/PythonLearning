#最大値最小化問題
#https://paiza.jp/works/mondai/binary_search/binary_search__application_step3
L, n, k = map(int, input().split())
A = [int(x) for x in input().split()]

A = [0] + A + [L]
left, right = 0, L
for i in range(1, k + 2):
    left = max(left, A[i] - A[i - 1])

left -= 1
while right - left > 1:
    mid = (left + right) // 2

    last_index, index, parts = 0, 0, 0
    while True:
        while index + 1 < k + 2 and A[index + 1] - A[last_index] <= mid:
            index += 1
        parts += 1
        if index == k + 1:
            break
        last_index = index
    if parts > n:
        left = mid
    else:
        right = mid

print(right)
