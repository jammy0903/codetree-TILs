import sys
input = sys.stdin.readline
import heapq
col,row = map(int,input().split())
imap = [list(map(int,input().rstrip()))for _ in range(row)]
dist = [[float('inf')]*col for _ in range(row)]

pq = []
heapq.heappush(pq,(0,(0,0))) #여태까지의 가중치,현재위치 
dist[0][0] = 0

while(pq):
    untilw, (xrow,xcol) = heapq.heappop(pq)

    if untilw < dist[xrow][xcol]:
        continue
    
    for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
        nr = xrow + dr
        nc = xcol + dc
       
        if 0<=nr<row and 0<=nc<col :
            
            cost = imap[nr][nc] + untilw
            if cost < dist[nr][nc]:
                dist[nr][nc] = cost 
               
                heapq.heappush(pq,(cost,(nr,nc)))
print(dist[row-1][col-1])
            
        