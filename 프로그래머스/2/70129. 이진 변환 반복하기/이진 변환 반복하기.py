def solution(s):
    count =0
    zero =0
    while 1:
        answer = ''
        if  s=="1":
            return [count, zero]
            
            
        for i in s:
            if i != "0":
                answer+=i
            if i =="0":
                zero+=1
        
        s = bin(len(answer))[2:]
        count+=1
   