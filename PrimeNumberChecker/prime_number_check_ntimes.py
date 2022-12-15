#複数の自然数の素数判定する場合、一回一回素数判定していると効率が悪いので、あらかじめ問題の範囲内の自然数をエラトステネスの篩を用いて素数判定しておく。
#N <= 6,000,000
N = int(input())

is_prime = [True] * 6000001
is_prime[0] = False
is_prime[1] = False

for i in range(2, 6000001):
    if is_prime[i]:
        for j in range(i * 2, 6000001, i):
            is_prime[j] = False

for _ in range(N):
    A = int(input())
    if is_prime[A]:
        print("pass")
    else:
        print("failure")
