#人数n
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
#dp[n] は人 n(n番目の人） が右端となっているような背の順区間のうち、最長であるような区間の長さ
dp = [1] * n
for i in range(1, n):
    if a[i-1] <= a[i]: #背の順である
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = 1
print(max(dp))
