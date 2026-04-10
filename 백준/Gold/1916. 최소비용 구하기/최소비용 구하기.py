from sys import stdin
import heapq
input = stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    s,d,w = map(int,input().split())
    graph[s].append((w,d))
src,dsc = map(int,input().split())


dt = [float('inf')]*(N+1)


pq = []
dt[src]=0
heapq.heappush(pq,(0,src))
while (pq):
    w_total, now = heapq.heappop(pq)
    if dt[now] < w_total:
        continue
    
    for now_w,nxt in graph[now]:
        cost = w_total +now_w
        if cost<dt[nxt]:
            dt[nxt] = cost
            heapq.heappush(pq,(cost,nxt))
if dsc <= N:
    print(dt[dsc])
else:
    print("Target node index out of range")