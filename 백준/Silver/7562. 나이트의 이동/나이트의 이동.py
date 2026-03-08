from collections import deque

# 1. 나이트가 이동할 수 있는 8가지 방향 (L자 모양)
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    # 체스판 크기 입력
    l = int(input())
    # 현재 나이트 위치 (시작점)
    start_x, start_y = map(int, input().split())
    # 목표 위치 (도착점)
    end_x, end_y = map(int, input().split())

    # 시작점과 도착점이 같으면 이동할 필요가 없으므로 0 출력
    if start_x == end_x and start_y == end_y:
        print(0)
        return

    # 방문 여부와 거리를 저장할 체스판 (0으로 초기화)
    # matrix[x][y]에는 시작점에서 해당 칸까지 오는 '최소 횟수'가 저장됨
    matrix = [[0] * l for _ in range(l)]
    
    # BFS를 위한 큐 생성 및 시작점 넣기
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft() # 큐에서 현재 위치를 꺼냄

        # 목표 지점에 도달했다면 정답 출력 후 종료
        if x == end_x and y == end_y:
            print(matrix[x][y])
            return

        # 8방향으로 발차기 시도!
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 1. 체스판 범위 안에 있고
            if 0 <= nx < l and 0 <= ny < l:
                # 2. 아직 한 번도 가보지 않은 칸이라면 (값이 0이라면)
                if matrix[nx][ny] == 0:
                    # 이전 칸의 이동 횟수 + 1 을 저장
                    matrix[nx][ny] = matrix[x][y] + 1
                    # 다음 탐색을 위해 큐에 넣기
                    queue.append((nx, ny))

# 테스트 케이스 개수 입력
t = int(input())
for _ in range(t):
    bfs()