import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
map = [list(map(int,input().strip())) for _ in range(n)]
from collections import deque
#시작점은 0,0
que = deque()

que.append((0,0))
map[0][0] = 0
while(que):
    r,c = que.popleft()
    for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        nr = r + dr
        nc = c + dc
        
        if 0<=nr<n and 0<=nc<m :
            if map[nr][nc] == 1:
                que.append((nr,nc))
                map[nr][nc] = map[r][c]+1
print(map[n-1][m-1]+1)