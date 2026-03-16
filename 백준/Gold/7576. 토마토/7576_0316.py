from sys import stdin
from collections import deque

input = stdin.readline

# 문제 입력은 "M N" 순서입니다.
# M = 가로 칸 수(열 개수), N = 세로 칸 수(행 개수) 입니다.
# 헷갈리기 쉬우므로 변수 이름도 cols, rows로 분리해 두는 편이 안전합니다.
cols, rows = map(int, input().split())

# box[y][x] 형태로 사용할 것이므로, rows개 줄을 입력받습니다.
box = [list(map(int, input().split())) for _ in range(rows)]

# BFS 큐에는 "현재 이미 익어 있는 토마토들"을 모두 넣습니다.
# 이 문제의 핵심은 시작점이 하나가 아니라 여러 개라는 점입니다.
# 즉, 토마토가 한 칸씩 차례대로 퍼지는 것이 아니라
# "처음부터 익어 있던 모든 토마토가 동시에 퍼져 나간다"라고 해석해야 합니다.
queue = deque()

# 상, 하, 좌, 우 네 방향 이동
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 1. 처음부터 익어 있는 모든 토마토를 큐에 넣습니다.
# 이렇게 해야 하루 단위로 "동시에" 퍼지는 BFS가 됩니다.
for y in range(rows):
    for x in range(cols):
        if box[y][x] == 1:
            queue.append((y, x))


def bfs():
    # 큐에서 하나를 꺼내고, 그 토마토가 주변 4칸을 익게 만듭니다.
    while queue:
        now_y, now_x = queue.popleft()

        for dy, dx in directions:
            next_y = now_y + dy
            next_x = now_x + dx

            # 배열 범위를 벗어나면 볼 수 없습니다.
            if not (0 <= next_y < rows and 0 <= next_x < cols):
                continue

            # 아직 익지 않은 토마토(0)만 다음 날 익힐 수 있습니다.
            if box[next_y][next_x] == 0:
                # "현재 칸의 날짜 + 1"을 저장합니다.
                # 처음 익어 있던 토마토는 1이므로,
                # 그 옆 칸은 2, 그 다음은 3 ... 이런 식으로 기록됩니다.
                # 즉, box 자체를 방문 처리 + 날짜 기록 용도로 함께 쓰는 방식입니다.
                box[next_y][next_x] = box[now_y][now_x] + 1
                queue.append((next_y, next_x))


bfs()


# 2. BFS가 끝난 뒤 결과를 판정합니다.
# 아직 0이 남아 있으면 끝까지 익지 못한 토마토가 있다는 뜻이므로 -1 입니다.
# 그렇지 않다면 가장 큰 값이 "가장 늦게 익은 날짜"입니다.
max_day = 1

for row in box:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit()
        max_day = max(max_day, tomato)


# 처음부터 익어 있던 토마토가 1이었으므로,
# 실제 걸린 날짜는 (가장 큰 값 - 1) 입니다.
# 예를 들어 전부 처음부터 익어 있었다면 max_day는 1이고, 정답은 0일입니다.
print(max_day - 1)
