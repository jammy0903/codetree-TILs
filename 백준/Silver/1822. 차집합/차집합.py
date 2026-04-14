import sys
input = sys.stdin.readline

# 입력 받기
nA, nB = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

# 차집합 계산
result = sorted(setA - setB)

# 출력
print(len(result))
if result:
    print(*result)
