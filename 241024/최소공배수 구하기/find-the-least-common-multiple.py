def lcm(a, b):
    return abs(a * b) // gcd(a, b)
from math import gcd

# 입력값을 정수로 변환
arr = list(map(int, input().split()))
arr.sort()

def fuin(n, m):
    if (m % n == 0):
        print(m)
    elif gcd(n, m) == 1:
        print(n * m)
    else:
        print(lcm(n, m))
    return 0

# 함수 호출
fuin(arr[0], arr[1])