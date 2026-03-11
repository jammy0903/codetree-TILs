import sys 
from collections import deque 
input = sys.stdin.readline
N,K = map(int,input().split())
street = [-1]*100001

que = deque()

def BFS(time,N):
    if N == K : 
        print(time)
        return 
    time = 0
    street[N] = time
    que.append((time,N))
    
    while(que):
        curtime, cur = que.popleft()
        if cur == K :
            print(curtime)
        for _ in range(3):
            plus_cur= cur+1
            minus_cur = cur-1
            multi_cur = cur*2
            if 0<=plus_cur<=100000 and street[plus_cur] == -1:
                street[plus_cur] = curtime+1
                que.append((street[plus_cur],plus_cur))
            if 0<=minus_cur<=100000 and street[minus_cur] == -1:
                street[minus_cur] = curtime+1
                que.append((curtime+1,minus_cur))
            if 0<=multi_cur<=100000 and street[multi_cur] == -1:
                street[multi_cur] = curtime+1
                que.append((curtime+1,multi_cur))
            
BFS(0,N)