#https://paiza.jp/works/mondai/binary_search/binary_search__basic_boss
#ある範囲に含まれている整数の個数を求める問題
#A_i >= k を満たす最小の i を返す
#A_i >= k を満たす i が存在しない場合は n を返す
def binarySearchMin(A, n, k_l):
    """A_i >= k_l を満たす最小の i を返す
    A_i >= k_l を満たす i が存在しない場合は n を返す"""
    # 探索範囲 [left, right]
    left = 0
    right = n
    #探索範囲を狭めていく
    while left < right:
        # 探索範囲の中央
        mid = (left + right) // 2

        if A[mid] < k_l:
            # a[0] ~ a[mid] は k 未満なので調べる必要が無い
            left = mid + 1
        else:
            right = mid
    
    return right
def binarySearchMax(A, n, k_r):
    """A_i >= k_r を満たす最小の i を返す
    A_i >= k_r を満たす i が存在しない場合は n を返す"""
    # 探索範囲 [left, right]
    left = 0
    right = n
    #探索範囲を狭めていく
    while left < right:
        # 探索範囲の中央
        mid = (left + right) // 2

        if A[mid] <= k_r:
            # a[0] ~ a[mid] は k 未満なので調べる必要が無い
            left = mid + 1
        else:
            right = mid
    
    return left
#数列の要素数n
n = int(input())
#数列A
A = list(map(int, input().split()))
A.sort()
#探索回数m
m = int(input())
#探索
for _ in range(m):
    #最小値K_l最大値k_r
    k_l, k_r = map(int, input().split())
    k_l, k_r = map(int, input().split())
    s = binarySearchMax(A, n, k_r)
    t = binarySearchMin(A, s, k_l)
    print(s - t)
