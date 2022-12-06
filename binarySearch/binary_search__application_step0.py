#この問題には、長さ x のパイプを k 本切り出せるなら、y ≦ x を満たすすべての y について長さ y のパイプを k 本切り出すことができるという単調性があります。
#従って、二分探索により 切り出せる/切り出せない 長さの境界を求めれば良いです。
#探索範囲が [left, right) のとき、長さ mid = (left+right)/2 のパイプを k 本切り出すことができるかどうかをチェックします(これは O(n) で実行可能です)。
#切り出すことができるなら、y ≦ mid を満たすすべての y について長さ y のパイプを k 本切り出せることがわかるため、探索範囲の左端を left から mid にします。
#逆に切り出すことができないならば、y >= mid を満たすすべての y について長さ y のパイプを k 本切り出せないことがわかるため、探索範囲の右端を right から mid にします。

A = [int(x) for x in input().split()]

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
