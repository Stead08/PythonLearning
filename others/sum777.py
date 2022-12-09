#https://paiza.jp/works/mondai/forest_contest_003/forest_contest_003__b_lucky_number
#足して777になる数字の組み合わせを出す。
#組み合わせが２個以上の場合multiple answersと出力
#初めてsysライブラリを入れた 
import itertools
import sys
n = int(input())
#n[0] to n[n-1]
n_l = [int(input()) for _ in range(n)]
ans = []
#候補の数字がもともと一つしかなくかつそれが777だった場合、それを出力してプログラム終了
if n == 1 and 777 in n_l:
    print(777)
    sys.exit()
else:
    for i in range(2, n+1):
        for v in itertools.combinations(n_l , i):
            if sum(v) == 777:　#任意の自然数に変更しても動作
               ans.append(v)
if len(ans) > 1:
    print("multiple answers")
elif len(ans) == 1:
    ans = sorted(ans[0])
    print(*ans)
else:
    print("no answer")
