def solution(num, total):
    answer = []
    if total%num==0:
        print(1)
        m = total//num
        print(m)
        for i in range(m-num//2, m+num//2+1):
            answer.append(i)
        
    else:
        print(0)
        m, n = total//num, total//num+1
        for i in range(m-num//2+1, n+num//2):
            answer.append(i)
        
    return answer
    