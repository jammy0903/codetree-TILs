import heapq
import sys
input = sys.stdin.readline
count = 0
while(True):
    N = int(input())
    if N == 0:
        break 
    grid = [list(map(int,input().split())) for _ in range(N)]
    distance_total = [[float('inf')]*N for _ in range(N)]
    #초기화 (grid[0],[0],0,0)
    pq = []
    distance_total[0][0] = grid[0][0]
    heapq.heappush(pq,(grid[0][0],0,0))
    #큐에 뭐 있는동안 계속 
    while(pq):

        weight_total,r,c = heapq.heappop(pq)
        if weight_total > distance_total[r][c]:
            continue
    
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr = r + dr
            nc = c + dc
            if 0<=nr<N and 0<=nc<N:
                cost = weight_total + grid[nr][nc]
                if cost<distance_total[nr][nc]:
                    distance_total[nr][nc] = cost
                    heapq.heappush(pq,(cost,nr,nc))
    count +=1
    print(f"Problem {count}: {distance_total[N-1][N-1]}")
            