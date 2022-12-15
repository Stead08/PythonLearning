#約数の個数をカウントする
from collections import defaultdict
#自然数N
N = int(input())

divisors = defaultdict(int)
for i in range(2, int(N ** 0.5) + 1):
    while N % i == 0:
        divisors[i] += 1
        N //= i

if N != 1:
    divisors[N] += 1

ans = 1
for k, v in divisors.items():
    ans *= v + 1

print(ans)
