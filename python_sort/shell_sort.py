#A:配列, n:Aの要素数, h:間隔
#挿入ソート
def insertion_sort(A, n, h):
    #アルゴリズムが正しく実装されていることを確認するために導入するカウンタ変数、ソート処理には関係がないことに注意
    num_of_move = 0
    
    for i in range(h, n):
        #A[i] を、整列済みの A[i-ah], ..., A[i-2h], A[i-h] の適切な位置に挿入する
        x = A[i]
        j = i - h
        #A[i] の適切な挿入位置が見つかるまで、A[i] より大きい要素を後ろにずらしていく
        while j >= 0 and A[j] > x:
            A[j+h] = A[j]
            j -= h
            num_of_move += 1
        #A[i]を挿入
        A[j+h] = x
    return A    
#シェルソート
#挿入の間隔を適当に決めてシェルソート
def shell_sort(A, n, H ):
    for h in H:
        insertion_sort(A, n, h)
    print(A)
#数列の長さn
n = int(input())
#数列
A = list(map(int, input().split()))
#間隔hの要素数
k = int(input())
#間隔のリスト
h = list(map(int, input().split()))
#シェルソートを実行
shell_sort(A, n, h)
