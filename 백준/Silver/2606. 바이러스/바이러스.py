import sys
from collections import deque
input = sys.stdin.readline
que = deque()
n = int(input())
m = int(input())

graph= [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False for _ in range(n+1)]
def bfs(start):
    cnt = 0
    que.append(start)
    visited[start] = True
    while(que):
        curr = que.popleft()
        
        for nei in graph[curr]:
            if not visited[nei]:
                visited[nei] = True
                que.append(nei)
                cnt +=1
               

    return cnt

print(bfs(1))