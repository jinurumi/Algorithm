def solution(date1, date2):
    answer = 0
    for d in range(len(date1)):
        date1[d] = date1[d] - date2[d]
        # 양수면 date1이 나중, 음수면 date1이 앞섬
    print(date1)

    if date1[0] > 0 :
        return 0
            
    elif date1[0] == 0:
        if date1[1] < 0 :
            return 1
        elif date1[1] == 0:
            if date1[2] <0:
                return 1
    elif date1[0] < 0 :
        return 1
       
    return 0 #date2 ->1