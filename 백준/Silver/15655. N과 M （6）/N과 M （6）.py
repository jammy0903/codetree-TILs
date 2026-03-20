import sys
input = sys.stdin.readline
answerSet = set()
N,line =map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

visited = [False]*(N)

answer = []
def DFS(start,depth):

    if depth == line:
        print(*(answer))
        return 
    for i in range(start,N): 
        if  visited[i] == False :
            visited[i] = True
            answer.append(arr[i])

            DFS(i,depth+1)
            visited[i] = False
            answer.pop()
DFS(0,0)


            
             