def solution(n):
    f=[0,1]
    
    # f 함수만들기
    for i in range(0,n+1):
        ff=f[i] + f[i+1]
        f.append(ff)

    return f[n]%1234567
    