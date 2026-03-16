h1, m1, h2, m2 = map(int, input().split())

# Please write your code here.
cnt = 0
while True:
    
    if h1 ==h2 and m1 == m2 : break

    m1 +=1
    cnt +=1
    if m1==60:
        
        h1+=1
        m1=0
h = h2-h1

print(cnt)