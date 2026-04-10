import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
total = 0
at = 0
for i in range(N):
    at +=arr[i]
    total +=at
    
print(total)
    
#1 2 3 3 4
#result_cp:1,
#result : 1