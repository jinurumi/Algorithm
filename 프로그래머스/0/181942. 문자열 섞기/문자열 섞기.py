def solution(str1, str2):
    answer = ''
    for s in range(len(str1)):
        answer += str1[s]
        answer += str2[s]
    return answer