import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T): # 테스트 케이스 수만큼 반복
    P = input().rstrip() # 수행할 함수 목록을 입력받음
    N = int(input()) # 배열의 크기를 입력받음
    dqs = input().rstrip()# 배열의 원소들을 입력받음
    dqs = dqs[1:-1]# 대괄호 제거
    flag = False # R 명령어의 수행 여부를 나타내는 플래그, False는 뒤집히지 않은 상태, True는 뒤집힌 상태
    dq = deque(map(int, dqs.split(','))) if dqs else deque()# 원소들을 콤마로 분리하여 정수로 변환한 후 deque에 저장, 빈 배열인 경우 빈 deque 생성
    for p in P:# 수행할 함수 목록을 하나씩 순회(명령어)
        if p == 'R':# R 명령어인 경우, dq를 뒤집음
            flag = not flag
        elif p == 'D':# D 명령어인 경우, dq에서 맨 앞의 원소를 제거
            if not dq:
                print('error')
                break
            if flag:
                dq.pop()
            else:
                dq.popleft()
        
    else:
        if flag:
            dq.reverse()
        print('[' + ','.join(map(str, dq)) + ']')
    

