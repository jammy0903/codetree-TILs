import sys
from collections import deque
input = sys.stdin.readline
#n m 을 입력받음 
N , M = map(int, input().split())
#그래프 라는 이름의 이차원 배열 이름을 할당 
graph=[]
#y 이동 x 이동 배열변수 생성 
dy = [0,0,+1,-1]
dx = [+1,-1,0,0]
#큐 생성 
que = deque()
#지도 입력받아서 바로 저장할 코드 생성 

for i in range(N):
    graph.append(list(map(int,input().split())))


#지도 개수 변수 선언
map_cnt = 0
#지도 사이즈 변수 선언(제일 큰 사이즈만 저장)
max_size = 0

#BFS 함수 선언 
def BFS(n,m):
    size = 0
#사이즈 변수 선언-1씩 늘어갈 예정
    global que 
    graph[n][m] = 2
    que.append((n,m))
#큐에 1인 것 추가해야하니까 추가함수 넣기
    while que : 
#큐에 뭔가 존재할때만 #큐에서 popleft해서 
        n , m = que.popleft()
        size += 1#사이즈 +1 함   
        for idx in range(4):
        #BFS하려면 4번 돌기  que에서 꺼낸 애를 기준으로. 
            ny = n + dy[idx]
            #새로운 y 는 기존 y 에다 움직임 변수 하나씩
            nx = m + dx[idx] 
            #새로운 x 는 기존 x 에다 움직임 변수 하나씩 
            if  0<= ny < N and 0<= nx  < M and graph[ny][nx] == 1 : 
            #근데 만약 벽일수도있으니까. 벽이 아닌 경우에만
                graph[ny][nx] = 2 
                #벽이 아니고 땅 맞으면 
                    #새로운 땅에다가 2로 바꾸고 

                que.append((ny,nx))
                    #그것도 큐에 넣음 

    return size 



#이중 for문 n,m
for i in range(N):
    for j in range(M):
#돌면서 이제 땅인지 아닌지 감별하면서 다님. 1 이면 
        if graph[i][j] == 1:
            map_cnt +=1
            max_size = max(max_size,BFS(i,j))


print(map_cnt)
print( max_size)