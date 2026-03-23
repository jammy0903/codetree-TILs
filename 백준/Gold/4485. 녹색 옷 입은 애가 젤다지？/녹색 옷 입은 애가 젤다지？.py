import heapq
import sys
input = sys.stdin.readline

count = 0
while True:
    N = int(input())
    if N == 0:  # N이 0이면 종료
        break
    
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    distance_total = [[float('inf')]*N for _ in range(N)]
    distance_total[0][0] = grid[0][0]
    pq = []
    heapq.heappush(pq,(grid[0][0],0,0))

    while pq:
        total_weight,r,c = heapq.heappop(pq)
        if distance_total[r][c] < total_weight:
            continue
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = r+ dr
            nc = c +dc
            if 0<=nr<N and 0<=nc<N :
                cost = total_weight + grid[nr][nc]
                if cost < distance_total[nr][nc]:
                    distance_total[nr][nc] = cost
                    heapq.heappush(pq,(cost,nr,nc))
                    
    count +=1
    print(f"Problem {count}: {distance_total[N-1][N-1]}")
