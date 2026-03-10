import sys 
input = sys.stdin.readline

N,M = map(int,input().split())

visited = [False]*(N+1)
answer = []

def DFS(depth):
    if depth == M : 
        print(*(answer))
        return
    for i in range(1,N+1):
        if visited[i] == False:
            visited[i]=True
            answer.append(i)

            DFS(depth+1)
            
            visited[i] = False
            answer.pop()
            
            

    
DFS(0) 