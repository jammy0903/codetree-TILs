m1, d1, m2, d2 = map(int, input().split())

# 각 월의 일수
end = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt = 1

while not (d1 == d2 and m1 == m2):  # 목표날짜와 같아질 때까지
    
    if d1 == end[m1]:  # 현재 월의 마지막 날인 경우
        d1 = 1
        m1 += 1
    else:  # 월의 마지막 날이 아닌 경우
        d1 += 1
    
    cnt += 1

print(cnt)