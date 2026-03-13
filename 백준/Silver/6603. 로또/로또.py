import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# [1] DFS 함수를 미리 정의해둡니다.
def DFS(start, depth):
    # 종료 조건: 6개를 다 뽑았을 때
    if depth == 6:
        print(*answer)
        return
    

    # 반복문: 'start' 방(인덱스)부터 끝까지 확인
    for i in range(start, K):
        answer.append(S[i])      # 숫자를 담고
        DFS(i + 1, depth + 1)    # "나보다 뒷번호 방부터 골라"라고 하며 재귀 호출
        answer.pop()             # 돌아오면 방금 담은 숫자 빼기 (백트래킹)

# [2] 메인 루프
while True:
    num_list = list(map(int, input().split()))
    K = num_list[0]
    
    if K == 0:
        break
    
    S = num_list[1:] # 뽑을 후보 숫자들 (이미 정렬되어 들어오지만, 불안하면 S.sort() 추가)
    answer = []      # 숫자를 담을 장바구니
    
    DFS(0, 0)        # 0번 인덱스부터, 0개 뽑은 상태로 시작!
    print()          # 테스트 케이스 사이 빈 줄 출력