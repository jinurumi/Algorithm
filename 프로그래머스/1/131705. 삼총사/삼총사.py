def solution(number):
    answer = 0
    a=[]
    #number 3총사 구하기
    for i in range(len(number)):
        #a.append(number[i])
        for j in range(i+1,len(number)):
            #a.append(number[j])
            for h in range(j+1,len(number)):
                if number[i] + number[j]+ number[h] ==0:
                    a.append([number[i], number[j],number[h]])
            
    return len(a)
    
    