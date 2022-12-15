#フェルマーテスト
#1. a を 2 から N-1 までの数からランダムに選ぶ。
#2. N が a で割り切れる場合は N は素数でないと判定する。
#3. a^(N-1) を N で割ったあまりが 1 ならば N は素数、1 でない場合は素数でないと判定する。

n = int(input())

is_prime = True
a = 2
fermat = 1

if n % a == 0:
    is_prime = False
#a^(N-1) を N で割ったあまりを求めるには
#1. fermat に a を掛ける。
#2. fermat に 「fermat を N で割った余り」 を代入する。
for i in range(n - 1):
    fermat *= a
    fermat %= n

if fermat % n != 1:
    is_prime = False

if is_prime:
    print("YES")
else:
    print("NO")
