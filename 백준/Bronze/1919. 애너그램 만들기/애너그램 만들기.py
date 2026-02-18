one = list(input().lower())
two = list(input().lower()) #두 문자열을 입력받아서 각각 one, two list에 저장


one_list = [0] * 26
two_list = [0] * 26
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = list(alphabet) #알파벳 리스트 만들어서 인덱스 번호로 알파벳 개수 세기 위해서

for i in range(len(one)):
    for j in range(26):
        if one[i] == alphabet_list[j]: #one 문자열의 알파벳이 alphabet_list의 j번째 알파벳과 같으면
            one_list[j] += 1 #one_list의 j번째 인덱스에 1 더하기
for i in range(len(two)):
    for j in range(26):
        if two[i] == alphabet_list[j]: #two 문자열의 알파벳이 alphabet_list의 j번째 알파벳과 같으면
            two_list[j] += 1 #two_list의 j번째 인덱스에 1 더하기


        
answer = 0
for i in range(26):
    answer += abs(one_list[i] - two_list[i]) #one_list와 two_list의 각 인덱스의 차이의 절댓값을 answer에 더하기
    
print(answer)