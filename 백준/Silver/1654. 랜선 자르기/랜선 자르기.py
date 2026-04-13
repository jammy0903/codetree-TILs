import sys
input = sys.stdin.readline

lenline,need = map(int,input().split())
linearr = [int(input().rstrip()) for _ in range(lenline)]

top = int(max(linearr))
start = 1
end = top
result = 0
cnt = 0
while( start<=end  ): #찾을 때까지 계속한다. 못찾으면 포기 #
    
    mid = (start+end)//2
    cnt = 0
    for i in range(lenline):
        cnt += linearr[i]//mid
    if cnt < need :
        end = mid-1
    elif cnt >= need:
        result = mid
        start = mid + 1
    elif cnt == need:
        flag = 1
        break

print(result)
    



    