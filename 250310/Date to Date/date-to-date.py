m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
end = [0,31,28,31,30,31,30,31,30,31,31,30,31]

cnt = 1
m1end = end[m1]
m2end = end[m2]

while m1<=m2 :
    d1 +=1
    cnt+=1
    if d1 >= end[m1]:
        m1 += m1
        d1 = 0
        continue 
    elif m1==m2 and d1==d2:
        break

print(cnt)



