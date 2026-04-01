import sys 
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.reverse()
max = arr[0]
#print(arr)
minus_total=0
for i in range(1,N):
    if max > arr[i]:
        #print(f"{max}가{arr[i]}보다 커")
        max = arr[i]
    else : 
        minus = arr[i]-max+1
        #print(f"{max}가{arr[i]}보다 작으니까 ")
        arr[i] = arr[i] - (arr[i]-max+1)
        #print(f"{i+1}번쨰 숫자였던 방금껀 {arr[i]}가되고 ")
        minus_total += minus
        #print(f"총 뺀 수는{minus_total}")
        max = arr[i]
        
print(minus_total)