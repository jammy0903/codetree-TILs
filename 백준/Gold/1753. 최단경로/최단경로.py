import heapq
import sys
input = sys.stdin.readline

u,v = map(int,input().split())
start = int(input())
graph= [[] for i in range(u+1)]
for i in range(v):
    first , stop , w = map(int,input().split())
    graph[first].append((stop,w)) 

def dajkstra(start):
    pq = [(0,start)] # 시작점을 큐에 넣음 
    distance_total = [float('inf') for i in range(u+1)] #역대 최단거리 저장 배열
    distance_total[start]=0
    while pq:
        
        weight_total,now = heapq.heappop(pq) #젤 작은거 뽑았음 
        if distance_total[now] < weight_total:#근데 할머니일수도?
            continue
        for new_dist, new_w  in graph[now]:
            cost = new_w + weight_total
            if cost < distance_total[new_dist]:
                distance_total[new_dist] = cost
                heapq.heappush(pq,(cost,new_dist))
            
    return distance_total

result = dajkstra(start)    


for i in range(1,u+1):
    if result[i] == float('inf'):
        print('INF')
    else : print(result[i])



