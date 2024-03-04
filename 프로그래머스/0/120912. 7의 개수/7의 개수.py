def solution(array):
    answer = 0
    for a in range(len(array)):
        answer += list(str(array[a])).count("7")
    return answer