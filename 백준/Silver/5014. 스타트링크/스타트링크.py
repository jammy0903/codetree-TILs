import sys
from collections import deque 
input = sys.stdin.readline
Floor,now,togo,U,D = map(int,input().split())
cnt = 0
visited = [-1]*(Floor+1)

que=deque()
que.append(now)
visited[now]=0

found = False

while(que):
    X = que.popleft() #현재 위치 
    if X == togo :
        found = True
        break
    arr = [U,-D]
    for i in arr:
        new = X + i
        if 0<new<=Floor and visited[new] == -1 :
            visited[new] = visited[X] + 1
            que.append(new)
        
if not found:
    print("use the stairs")
else:
    print(visited[togo])
   
        