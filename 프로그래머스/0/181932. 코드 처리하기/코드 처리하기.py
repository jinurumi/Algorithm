def solution(code):
    mode = "0"
    answer = ''
    for idx, c in enumerate(code):
        # if c=='1':
        #     mode='1'
        print(mode)
        if mode =='0':
            if c!='1':
                if idx%2==0:
                    answer+=c
            else:
                mode = '1' 
        elif mode =='1':
            if c!='1':
                if idx%2==1:
                    answer+=c
            else:
                mode ='0'
    if len(answer)==0:
        return "EMPTY"
    return answer