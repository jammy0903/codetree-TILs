import sys
input = sys.stdin.readline

n,target = map(int,input().split())
trees=list(map(int,input().split()))
result = 0
start = 0
maxend = max(trees)
end = maxend
while(start<=end and end<=maxend):
    mid = (start+end)//2
    total = 0
    
    total = sum(tree - mid for tree in trees if tree > mid)
        
    
     
    if total >=target:
        result = mid
        start = mid + 1
    elif total < target:

        end = mid - 1
print(result)