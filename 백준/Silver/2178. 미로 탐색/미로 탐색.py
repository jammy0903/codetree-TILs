import sys 
input = sys.stdin.readline
from collections import deque
que= deque()
N,M = map(int,input().split())
grid = [list(map(int,input().rstrip()))for _ in range(N)]


def BFS(X,Y):

    if X == N-1 and Y == M-1 : 
        print(grid[X][Y])
    que.append((X,Y))
    
    while(que):
        curX , curY = que.popleft()
        if curX == N-1 and curY == M-1 : 
            print(grid[curX][curY])
    
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            newX = curX + dx
            newY = curY + dy
            if 0<=newX<N and 0<=newY<M and grid[newX][newY] == 1:
                
                grid[newX][newY] = grid[curX][curY]+1
                que.append((newX,newY))
                



BFS(0,0)