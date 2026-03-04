from collections import deque

# 1. 입력 받기 (M: 가로, N: 세로)
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

# 2. 핵심! 시작하기 전에 "익은 토마토(1)"를 모두 찾아서 큐에 넣기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 익은 토마토의 좌표(행, 열)를 큐에 미리 다 넣어둡니다.
            queue.append((i, j))

# 3. BFS 시작
def bfs():
    while queue:
        x, y = queue.popleft()
        
        # 상, 하, 좌, 우 확인용 좌표
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            
            # 격자 범위 안이고, 아직 안 익은 토마토(0)라면?
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 현재 날짜 + 1을 저장 (방문 처리 겸 날짜 기록)
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()

day = 0
for row in graph:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit()
        day = max(day,tomato)
print(day-1)
