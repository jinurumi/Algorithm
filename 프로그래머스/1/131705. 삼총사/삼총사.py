def solution(number):
    a=[]
    #number 3총사 구하기
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            for h in range(j+1,len(number)):
                if number[i] + number[j]+ number[h] ==0:
                    a.append([number[i], number[j],number[h]])
            
    return len(a)
    
    