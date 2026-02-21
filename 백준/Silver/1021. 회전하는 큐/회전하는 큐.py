import sys
input = sys.stdin.readline

N,M = map(int,input().split())

targets = map( int,input().split())
# 뽑아내려는 수들의 위치(타겟 리스트)를 입력받음
from collections import deque
# 2. 초기화
# 1부터 N까지의 숫자가 담긴 deque를 생성
cd = deque()
for i in range(1,N+1):
    cd.append(i)
       
# 총 이동 횟수를 저장할 변수(answer)를 0으로 초기화
answer = 0
# 3. 타겟 숫자들을 하나씩 순회 (for target in targets:)
for target in targets:
    idx = cd.index(target)
    
    # 절반보다 앞에 있거나 정확히 중간이면 -> 왼쪽으로 당기기
    if idx <= len(cd) // 2:
        cd.rotate(-idx)    # 왼쪽으로 idx만큼 이동
        answer += idx      # 이동한 만큼 더하기
    
    # 절반보다 뒤에 있으면 -> 오른쪽으로 밀기
    else:
        move_right = len(cd) - idx
        cd.rotate(move_right) # 오른쪽으로 이동
        answer += move_right   # 이동한 만큼 더하기
        
    # 이제 맨 앞에 도착했으니 제거
    cd.popleft()
# 4. 최종 결과 출력
# answer(총 이동 횟수) 출력
print(answer)