#数列の長さ
n = int(input())
#数列を取得
l = list(map(int, input().split()))
#ソート済みの数列 A に 値 k が含まれているなら true を、含まれていないなら no を返す
def binarySearch(l, k, n):
    """数列l,探索数値k,数列の長さk"""
    #探索範囲：左端(left),右端(right)
    left = 0
    right = n - 1
    #探索範囲を狭めていく
    while left <= right:
        #数列の中央を求める
        mid = (left + right) // 2
        if l[mid] == k:
            return True
        elif l[mid] < k:
            left = mid + 1
        elif l[mid] > k:
            right = mid - 1
    return False
#入力される値について二部探索を実行
## 入力される値の量
m = int(input())
## for loop
for _ in range(m):
    t = int(input())
    if binarySearch(l, t, n) == True:
        print("Yes")
    else:
        print("No")
