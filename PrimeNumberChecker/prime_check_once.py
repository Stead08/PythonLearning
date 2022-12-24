# 2 以上の整数 N に対し、N が素数であれば true、素数でなければ false を返す関数
import math
def isPrime(N):
    N = round(math.sqrt(N))
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

n = int(input())
if isPrime(n) == True:
    print("{} is prime #".format(n))
else:
    print("{} is NOT prime #".format(n))
