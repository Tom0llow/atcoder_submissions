K = int(input())

MOD = 1000000007

if K % 9 != 0: 
    print(0)
    exit()

dp = [0]*(K+1)
dp[0] = 1

for i in range(1,K+1):
    B = min(i,9)
    for j in range(1,B+1):
        dp[i] += dp[i-j]
        dp[i] %= MOD

print(dp[K])

