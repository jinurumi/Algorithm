def solution(a, d, included):
    answer = 0
    for j in range(0, len(included)):        
        if included[j] == True:
            answer+=a + d *j
        
    return answer