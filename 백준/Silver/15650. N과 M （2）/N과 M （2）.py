import sys
input = sys.stdin.readline

n,m=map(int,input().split())
arr=[a for a in range(1,n+1)]
visited = [False]*(n+1)
answer = []

def DFS(start,depth):
    if depth == m:
        print(*(answer))
        return 
    for i in range(start,n+1):
        if visited[i] == False :
            visited[i] = True
            answer.append(i)
            DFS(i+1,depth +1)
            visited[i] = False
            answer.pop()
DFS(1,0)

            
             