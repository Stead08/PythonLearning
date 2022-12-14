#https://paiza.jp/works/mondai/sort_efficient/sort_efficient__quick
count = 0 #計算回数を記録しているだけ
# A[left] ~ A[right-1] をクイックソートする

#配列 A をクイックソートするには quick_sort(A, 0, n) を呼び出す

def quick_sort(A, left, right):
    global count
    #ソートする範囲の長さが一以下の場合は何もしない
    if left + 1 > right:
        return
    
    #データ列の末尾をピボットとする
    pivot = A[right -1]
    
    #ピボット未満のデータを挿入する位置を保持する変数
    cur_index = left
    
    for i in range(left, right - 1):
        if A[i] < pivot:
            A[cur_index], A[i] = A[i], A[cur_index]
            cur_index += 1
            count += 1
            
    #ピボットをA[cur_index] へ移動し、データ列を分割する
    A[cur_index], A[right - 1] = A[right - 1], A[cur_index]
    
    quick_sort(A, left, cur_index)
    quick_sort(A, cur_index + 1, right)
    
n = int(input())
A = list(map(int, input().split()))

quick_sort(A, 0, n)

print(*A)
    
