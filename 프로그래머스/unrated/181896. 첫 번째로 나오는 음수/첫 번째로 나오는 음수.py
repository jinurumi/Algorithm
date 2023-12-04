def solution(num_list):
    li=[]
    for num in num_list:
        if num<0:
            li.append(num_list.index(num))
    
    if len(li)==0:
        return -1
    else:
        return li[0]
