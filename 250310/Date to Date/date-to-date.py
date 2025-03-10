m1, d1, m2, d2 = map(int, input().split())

# 각 월의 일 수 (2011년은 윤년이 아님)
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 같은 달이면 단순히 날짜 차이 계산
if m1 == m2:
    print(d2 - d1 + 1)
else:
    # 첫 달의 남은 일수 + 마지막 달의 지난 일수 + 중간 달의 총 일수
    total_days = (days_in_month[m1] - d1 + 1) + d2
    for month in range(m1 + 1, m2):
        total_days += days_in_month[month]

    print(total_days)
