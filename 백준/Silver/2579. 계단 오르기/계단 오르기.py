import sys
input = sys.stdin.readline
n = int(input())
star = [0] + [int(input()) for _ in range(n)]
dp= [0]*301

dp[1]=star[1]
if n>=2:
    dp[2]=star[2] + dp[1]
if n>=3:
    dp[3]=max(star[3]+dp[1],star[2]+star[3])

for i in range(4,n+1):
    
    dp[i] = max(star[i]+star[i-1]+dp[i-3],star[i]+dp[i-2])
print(dp[n])
    