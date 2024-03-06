def solution(a, b, n):
    answer = 0 # 총 받은콜라
    
    while n >= a:
        answer += (n//a)*b
        n = (n-(n//a)*a + (n//a)*b)
    
    return answer