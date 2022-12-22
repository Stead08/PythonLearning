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
q = int(input())

A.sort()

for _ in range(q):
    l, r = map(int, input().split())
    #l以上の値が最初に現れる位置
    lpos = binary_search(A, n, l)
    #r以上の値が最初に現れる位置
    rpos = binary_search(A, n, r + 1)
    print(rpos - lpos)
