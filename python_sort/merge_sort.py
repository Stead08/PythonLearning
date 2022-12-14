#アルゴリズムが正しく実装されていることを確認するために導入するカウンタ変数、ソート処理には関係がないことに注意
# 部分データ列 A[left] ~ A[mid-1], A[mid] ~ A[right-1] はそれぞれ整列済み
# 2つの部分データ列をマージし、A[left] ~ A[right-1] を整列済みにする
#https://paiza.jp/works/mondai/sort_efficient/sort_efficient__merge
count = 0
INF = 1000000001

def merge(A, left, mid, right):
    global count
    L =A[left:mid]
    R = A[mid:right]
    L.append(INF)
    R.append(INF)
    
    #二つの部分データ列をマージしてA[left] ~ A[right]に書き込む
    lindex = 0
    rindex = 0
    
    for i in range(left , right):
        if L[lindex] < R[rindex]:
            A[i] = L[lindex]
            lindex += 1
        else:
            A[i] = R[rindex]
            rindex += 1
            count += 1
#   A[left] ~ A[right-1] をマージソートする


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2 
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

n = int(input())
A = list(map(int, input().split()))

# 配列 A をマージソートするには merge_sort(A, 0, n) を呼び出す
merge_sort(A, 0, n)

print(*A)
print(count)
