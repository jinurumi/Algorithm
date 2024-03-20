def solution(A,B):
    answer = 0
    
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    #for i in range(len(A)):
        
    return sum([A[i]*B[i] for i in range(len(A))])