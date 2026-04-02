import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# A는 오름차순
A.sort() 

# B는 내림차순 (reverse=True 옵션)
B.sort(reverse=True)
answer = 0
for i in range(N):
    answer +=A[i]*B[i]
print(answer)