import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque
que= deque()
N=int(input())
K = int(input())
num = []
for _ in range(N):
    num.append(input().rstrip())


visited = [False]*N

answer = set()
small_answer = []

def DFS(depth):
    if depth == K:
        answer.add("".join(small_answer))
        return
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            small_answer.append(num[i])
            DFS(depth +1)
            visited[i] = False
            small_answer.pop()
DFS(0)
print(len(answer))    
        

