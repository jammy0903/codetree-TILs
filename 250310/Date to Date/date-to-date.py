m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
end = [0,31,28,31,30,31,30,31,30,31,31,30,31]

day_cnt = 0


while m1 <= m2 :


    if m1 == m2 :
        if d1 == d2 : #정답 
            day_cnt +=1
            break

        elif d1 < d2 :
            d1 +=1
            day_cnt +=1
            continue

    elif m1 < m2  :
        if d1 < end[m1] :
            d1 +=1
            day_cnt +=1
            continue

        elif d1 == end[m1] : #경계선
            d1 = 1 # 1개월 올리자.
            m1 +=1
            day_cnt +=1
            continue
    
print(day_cnt)



