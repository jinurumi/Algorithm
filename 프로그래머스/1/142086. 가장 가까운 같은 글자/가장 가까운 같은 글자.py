def solution(s):
    answer = []
    
    for i in range(len(s)):
        #문자열 돌기
        #index = 0
        a= []
        for j in range(i-1,-1,-1):
            # 앞에 문자열 있는지 확인
            #print(i,j )
            if s[i] == s[j]:
                a.append(i-j)
                #print(1)
                break
                
        if len(a)==0:    
            answer.append(-1)
        else:    
            answer.extend(a)
    return answer