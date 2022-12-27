from math import gcd
# gcdモジュールは最大公約数


n = int(input())

ans = 1
for _ in range(n):
    a = int(input())
    #lcm(a, b) = a * b / gcd(a, b)の関係を用いる
    ans = ans * a // gcd(ans, a)

print(ans)
