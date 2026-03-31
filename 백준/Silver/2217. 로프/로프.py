import sys 
input = sys.stdin.readline
#lope개수입력 
N = int(input())
#개수만큼 한줄에 하나씩 입력 
lope=[int(input()) for _ in range(N)]
lope.sort(reverse=True)
lope.append(0)
new_lope=[]
for i in range(len(lope)-1):
    new_lope.append(lope[i]*(i+1))

new_lope.sort(reverse=True)
print(new_lope[0])