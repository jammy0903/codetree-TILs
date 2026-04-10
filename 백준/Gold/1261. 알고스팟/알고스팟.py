from sys import stdin
input = stdin.readline
import heapq

m,n = map(int,input().split())
imap = [list(map(int,input().strip())) for _ in range(n)]
weight = [[float('inf')]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]

dir = [(0,1),(0,-1),(1,0),(-1,0)]
pq = [] #pq = [w,x,y]
#초기값설정
weight[0][0] = 0     #dist=[0,inf,inf,inf,inf,,,,,inf]
heapq.heappush(pq,(0,0,0))

while(pq):
    w,x,y = heapq.heappop(pq) #큐에 넣어놓은 것 중 가장 가중치가 작은 걸 빼기 
    if weight[x][y]<w: #현재까지 최소값이라고 생각하는 w값이 지금 기록해놓은 곳의 가중치값보다 크면 의미없는거니까 지나가게함
        continue
        
    for dx,dy in dir: #현재 위치에서 4군데를 검색
        nx = x + dx
        ny = y + dy    
        #가중치 업데이트 계산
        if 0<=nx<n and 0<=ny<m and visit[nx][ny] == False:
            cost = w + imap[nx][ny]
            if weight[nx][ny] > cost : 
                weight[nx][ny] = cost
            heapq.heappush(pq,(cost,nx,ny))
            visit[nx][ny] = True
print(weight[n-1][m-1])
        
    
    
    
