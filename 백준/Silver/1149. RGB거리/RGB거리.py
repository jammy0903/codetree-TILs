from sys import stdin
input = stdin.readline
n = int(input())
imap = [list(map(int,input().split()))for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
R = 0
G=1
B=2
dp[0][R] = imap[0][0]
dp[0][G] = imap[0][1]
dp[0][B] = imap[0][2]

# 3. 2번 집부터 N번 집까지 계산
for i in range(1, n):
    # 빨강을 고를 때: 이전 집의 초록, 파랑 중 최솟값 + 현재 집 빨강 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + imap[i][0]
    
    # 초록을 고를 때: 이전 집의 빨강, 파랑 중 최솟값 + 현재 집 초록 비용
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + imap[i][1]
    
    # 파랑을 고를 때: 이전 집의 빨강, 초록 중 최솟값 + 현재 집 파랑 비용
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + imap[i][2]

# 4. 마지막 집까지 칠했을 때, 세 가지 색상 중 가장 저렴한 값 출력
print(min(dp[n-1]))
