import sys
input = sys.stdin.readline

n = int(input())
T = []
P = []

for _ in range(n):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
    
dp = [0]*(n+1)

for i in range(n-1,-1,-1):
    finday = i + T[i] #총 합 데이(n일넘기면 안되는)
    if finday <= n :
        dp[i] = max(P[i]+dp[finday],dp[i+1])
    else:
        dp[i] = dp[i+1]
        
print(dp[0])
    