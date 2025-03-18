m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
end = [0,31,28,31,30,31,30,31,30,31,31,30,31]

cnt = 1


while not ((d1==d2) and (m1==m2)) : # 목표날짜가 같은경우만 빼고 

   
    if m1 == m2: # 날만 다른거니까 
        d1 +=1
        cnt +=1
    elif m1 < m2:  # 월이 다른애들 
        if d1 == end[m1]: #그중 마지막 날인애들
            d1 =1
            m1 +=1
            cnt +=1
        else:#  아니면 d1이나 올리는 경우임
            d1 +=1
            cnt +=1

print(cnt)
     





    
    

