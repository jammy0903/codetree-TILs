N,K = map(int,input().split()) #N:물건의 수, K:배낭의 용량


dp = [0]*(K+1) 
for _ in range(N):
    w, v = map(int,input().split()) #w:물건의 무게, v:물건의 가치
    for i in range(K,w-1,-1): #역순이니까 w-1에서멈춰
        dp[i] = max(dp[i],dp[i-w]+v)
        
print(dp[K])
