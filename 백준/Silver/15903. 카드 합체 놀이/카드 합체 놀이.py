import heapq
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
hq = list(map(int,input().split()))
heapq.heapify(hq)
result = 0
new = 0
for _ in range(K):
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    c = a+b
    heapq.heappush(hq,c)
    heapq.heappush(hq,c)
    
while(hq):
    result +=heapq.heappop(hq)
print(result)