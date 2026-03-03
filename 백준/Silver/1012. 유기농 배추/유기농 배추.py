from sys import stdin
input = stdin.readline
from collections import deque


def bfs(x,y):
    que = deque()
    #현재 바닥이 배추인거니까 일단 visit,que, 상하좌우 확인해서 더 visit만들기 
    visit[x][y] = True
    que.append((x,y))
    needwarm = 1
    while(que):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        cx,cy = que.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1 and not visit[nx][ny]:
                que.append((nx,ny))
                visit[nx][ny] = True
    return needwarm


T = int(input()) #몇번 실행할건지
for _ in range(T):
    M,N , K = map(int,input().split()) #행 열 배추개수
    visit = [[False]*M for i in range(N)] #False 초기화 이중포문
    
    result_cnt = [] #결국 정답 배열 
    needwarm = 0 #bfs함수의 return용 변수
    
    graph = [[0]*M for i in range(N)] #배추밭 생성 가로가 M 세로가 N 
    
    #배추 개수만큼 입력받아야하니까 K만큼 for문.
    for _ in range(K):
        x,y = map(int,input().split()) # M 이 열이고 X , N이 행이고 y 
        graph[y][x] = 1 #행 열 구분 잘해 

            

    for i in range(N):
        for j in range(M):
            #배추밭에서 배추인 곳만 찾아가서 bfs시작할수있게 하기 
            if graph[i][j] == 1 and not visit[i][j] : 

                result_cnt.append(bfs(i,j))
            
    print(len(result_cnt))
            