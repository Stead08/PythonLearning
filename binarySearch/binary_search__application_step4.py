#https://paiza.jp/works/mondai/binary_search/binary_search__application_boss
#二部探索の関数を作成
def binary_search(A, n, k):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if A[mid] < k:
            left = mid + 1
        else:
            right = mid

    return right


n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
B = [int(x) for x in input().split()]
k = int(input())

B.sort()
left, right = -1, 200000000
while right - left > 1:
    mid = (left + right) // 2
    smaller = 0
    for i in range(n):
        smaller += binary_search(B, len(B), A[i] + mid + 1) - binary_search(
            B, len(B), A[i] - mid
        )

    if smaller < k:
        left = mid
    else:
        right = mid

print(right)
