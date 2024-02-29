def solution(intStrs, k, s, l):
    answer = []
    for ints in intStrs:
        answer.append(int(ints[s:s+l]))
        
    
    return [x for x in answer if x>k]