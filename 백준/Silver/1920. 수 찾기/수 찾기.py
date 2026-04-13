import sys
input = sys.stdin.readline
#n은 정렬하며 입력받는다
n = int(input())
nlist =sorted(list(map(int,input().split())))
#있는지 없는지 판단할 리스트 받기
target_cnt= int(input())
target_arr = list(map(int,input().split()))


def bs(target,si,ei):
    while(si<=ei): #첫값이 끝값보다 작거나 같을떄만 진행해 
        mididx = (si+ei)//2
        if nlist[mididx] == target:
            return (True)
        elif nlist[mididx] > target:
            ei = mididx -1
        else :
            si = mididx +1
    return False
    
for i in target_arr:
    sidx = 0
    eidx = n-1
    if bs(i,sidx,eidx) == True:
        print(1)
    else:
        print(0)



    