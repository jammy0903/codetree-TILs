import sys
from collections import deque
input = sys.stdin.readline
que = deque()

n,mid = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(mid):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt =0
visited = [False for _ in range(n+1)]
def bfs(start):
    if visited[start] == True:
        return False
    visited[start] = True
    que.append(start)
    while(que):
        curr = que.popleft()
        for i in graph[curr]:
            if visited[i] == False:
                que.append(i)
                visited[i] = True
                
    return True
for i in range(1,n+1):
    if bfs(i) :
        cnt +=1
    
print(cnt)