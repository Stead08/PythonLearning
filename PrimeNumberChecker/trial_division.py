n = int(input())
def trial_division(n):
    if n < 2:
        return []
    #素因数
    prime_factors = []
     
    for i in range(2, int(n ** 0.5) + 1):
        #nがiで割り切れる場合、iを素因数としてリストに追加
        while n % i == 0:
            prime_factors.append(i)
        # nをiで割った商で更新 （例えば6が２で割り切れる場合次は２で割った３から分解を始めるってこと）
            n //= i
        
        # nの平方根より大きい素因数が存在する場合
    if n > 1:
        prime_factors.append(n)
            
    return prime_factors
        
ans = trial_division(n)
for i in ans:
    print(i)
        
        
    
