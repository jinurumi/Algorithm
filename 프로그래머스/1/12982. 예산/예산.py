def solution(d, budget):
    answer = 0   
    d= sorted(d)
    for i in range(len(d)):
        answer+=d[i]
        print(budget , answer)
        if budget < answer:
            return i
        if budget == answer:
            return i+1
    return len(d)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #     a= []
#     d = sorted(d)
#     for i in range(len(d)):
#         a.append(d[i])
#         d.pop(d[i])
#         for j in range(len(d)):
#             a.append(d[j])
#             d.pop(d[j])
#             if sum(a) > 9:
#                 break
#                 for h in range(len(d)):
#                     a.append(d[h])
#                     d.pop(d[h])
#                     if sum(a) > 9:
#                         break
            
            
#     return len(a)