def solution(num_list):
    if len(num_list)>=11:
        su=0
        for num in num_list:
            su+=num
    else:
        su=1
        for num in num_list:
            su*=num
    return su