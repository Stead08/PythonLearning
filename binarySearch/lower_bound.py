#https://paiza.jp/works/mondai/binary_search/binary_search__basic_step1
#A_i >= k を満たす最小の i を返す
#A_i >= k を満たす i が存在しない場合は n を返す
def binarySearch(A, n, k):
    """A_i >= k を満たす最小の i を返す
    A_i >= k を満たす i が存在しない場合は n を返す"""
    # 探索範囲 [left, right]
    left = 0
    right = n
    #探索範囲を狭めていく
    while left < right:
        # 探索範囲の中央
        mid = (left + right) // 2

        if A[mid] < k:
            # a[0] ~ a[mid] は k 未満なので調べる必要が無い
            left = mid + 1
        else:
            right = mid
    
    return right

#数列の要素数n
n = int(input())
#数列A
A = list(map(int, input().split()))
A.sort()
#探索回数m
m = int(input())
#探索
for _ in range(m):
    s = int(input())
    print(n - binarySearch(A, n, s))
