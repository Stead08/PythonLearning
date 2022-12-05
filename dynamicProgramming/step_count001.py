#階段を上るのに、1歩で a 段または b 段または c 段を上ることができるとき、n 段の階段を上る方法は何通りあるか
#段数n, a,b,c段飛ばし
#a,bの二通りで考えたい場合はcに関係する文を削除
n, a, b, c = map(int, input().split())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    if i >= a:
        dp[i] += dp[i-a]  # i-a 段目からa段上って i 段へ到達
    if i >= b:
        dp[i] += dp[i-b] #i-b 段目からb段上って i 段へ到達
    if i >= c:
        dp[i] += dp[i-c] #i-c 段目からc段上って i 段へ到達
print(dp[n]) 
