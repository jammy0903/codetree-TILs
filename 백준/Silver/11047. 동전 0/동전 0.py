import sys 
input = sys.stdin.readline


N ,K = map(int,input().split())
coin=[int(input()) for _ in range(N)]
coin.sort(reverse=True)

cnt = 0

for i in range(len(coin)):
    if K == 0:
        break
        
    cnt += K//coin[i] #동전개수 업데이트
    K %= coin[i] #남은돈 업데이트
print(cnt)


