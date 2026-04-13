import sys 
input = sys.stdin.readline
n,target = map(int,input().split())
lines = [int(input().rstrip())for _ in range(n)]

start = 1
end = max(lines)
result = 0

while(start<=end):
    cnt = 0
    length = (start+end)//2
    
    for i in range(n):
        cnt += lines[i]//length 
        
    if cnt >= target:
        result = length #후보
        start = length + 1
    else : 
        end = length - 1
    
print(result)
        