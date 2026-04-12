'''
입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
search_list=sorted(list(map(int,input().split()))) # 1 2 3 4 5 
m=int(input())
target_list=list(map(int,input().split())) #1 3 7 9 5

for i in range(m):
    start = 0
    end = n-1
    target = target_list[i] # 지금 선수입장 어디서? target_list에서 
    flag = 0
    while(start<=end):
        mididx = (start+end) // 2 #searchlist에서 중간idx 구함 
        if search_list[mididx] == target: # 그 idx를가진 중간값이 혹시..답? 
            print(1)
            flag = 1
            break
        elif search_list[mididx] < target: #r 으로 가자 
            start = mididx + 1
        elif search_list[mididx] > target: #왼쪽
            end = mididx -1
    if flag == 0 :
        print(0)   
            
         
