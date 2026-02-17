
N,X = map(int,input().split()) #N:수열의 크기 X:제일큰 수 
arr=list(map(int,input().split()))  #수열 입력받아서 리스트로 바꿈 

for i in range(N):
    if arr[i] < X : #수열의 원소가 X보다 작은 경우 
        print(arr[i],end=' ') #출력할 때 띄어쓰기
