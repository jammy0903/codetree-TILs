def solution(numbers, target):
    answer = 0

    def dfs(idx, current_sum):
        if idx == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
        
        # current_current_sum -> current_sum 으로 오타 수정 완료!
        addcase = dfs(idx + 1, current_sum + numbers[idx])
        subcase = dfs(idx + 1, current_sum - numbers[idx])
        
        return addcase + subcase 
        
    answer = dfs(0, 0)
    return answer

# 맨 밑에 있던 solution(numbers,target) 호출 부분은 깔끔하게 삭제했습니다!