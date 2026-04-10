import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
map = [list(map(int,input().split())) for _ in range(N)]

max_val = max(max(row) for row in map)
result = []
def BFS(x,y,n,visited):
    que = deque()
    que.append((x,y))
    visited[x][y] = True
    while(que):
        curx,cury = que.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)] :
            nx = curx + dx
            ny = cury + dy 
            if 0<=nx<N and 0<=ny<N and map[nx][ny]>n and visited[nx][ny] == False:
                visited[nx][ny] = True
                que.append((nx,ny))
    
def func(n): # n은 현재 비의 높이
    visited = [[False] * N for _ in range(N)]
    count = 0  # 안전 영역의 개수를 저장할 변수
    
    for i in range(N):
        for j in range(N):
            # 1. 물에 잠기지 않았고(map[i][j] > n)
            # 2. 아직 방문하지 않았다면 (not visited[i][j])
            if map[i][j] > n and not visited[i][j]:
                # 여기서 BFS를 실행해서 연결된 모든 땅을 방문 처리!
                BFS(i, j, n, visited) 
                count += 1 # BFS가 한 번 끝나면 영역 하나를 다 찾은 것이므로 +1
                
    return count # 최종적으로 이 높이(n)에서 찾은 총 영역 개수 반환

# 메인 루프
for i in range(max_val):
    result.append(func(i))

# 결과 출력 (리스트 중 가장 큰 값)
print(max(result))