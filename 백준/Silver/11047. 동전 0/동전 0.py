import sys
input = sys.stdin.readline

N,K = map(int,input().split())
coin=[int(input()) for _ in range(N)]
coin.sort(reverse=True)
cnt = 0
for i in range(N):
    cnt +=K // coin[i]
    K %= coin[i]
print(cnt)