def solution(numer1, denom1, numer2, denom2):
    mo = denom1*denom2 # 분모
    ja1 = numer1*denom2 # 분자1
    ja2 = numer2*denom1 # 분자2
    ja = ja1+ja2
    print(ja, mo)
    
    for i in range(1,1001):
        if ja%i ==0 and mo%i==0:
            print(i,"i")
            ja /= i 
            mo /= i
    
    for i in range(1,1001):
        if ja%i ==0 and mo%i==0:
            print(i,"i")
            ja /= i 
            mo /= i
    return [ja,mo]
    