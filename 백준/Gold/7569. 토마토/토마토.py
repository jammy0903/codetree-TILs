import sys
input = sys.stdin.readline
from collections import deque

# r: 세로(N), c: 가로(M), h: 높이(H)
c, r, h = map(int, input().split())

# 3중 리스트 컴프리헨션
board = [[list(map(int, input().split())) for _ in range(r)] for _ in range(h)]
que = deque()

for i in range(h):
    for j in range(r):
        for x in range(c):
            
            if board[i][j][x] == 1:
                que.append((i,j,x))
                
while(que):
    ch,cr,cc = que.popleft()
    for dh,dr,dc in [(-1,0,0),(1,0,0),(0,0,1),(0,-1,0),(0,0,-1),(0,1,0)]:
        nh = ch + dh
        nr = cr + dr
        nc = cc + dc
        if 0<=nh<h and 0<=nr<r and 0<=nc<c and board[nh][nr][nc] == 0 :
            next_cnt = board[ch][cr][cc] + 1
            board[nh][nr][nc] = next_cnt
            que.append((nh,nr,nc))

max_day = 0
for layer in board:
    for row in layer:
        for tomato in row:
            if tomato == 0:
                print(-1)
                exit()
            max_day = max(max_day,tomato)
print(max_day-1)