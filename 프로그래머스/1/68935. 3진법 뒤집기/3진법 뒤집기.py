def solution(n):
    a,b = [],[]
    
    for i in range(16,-1,-1):
 
        a.append(n//3**i)
        n = n%3**i
    
    for i in range(len(a)):
        if a[i]!=0:
            b = a[i:]
            break
            
    print(b)
    b = ''.join(map(str,b[::-1]))
    print(b)
    b=int(b,3)
        
    return b
    
