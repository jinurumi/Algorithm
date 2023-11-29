def solution(rsp):
    li = ''
    for i in range(len(rsp)):
        if rsp[i]=='0':
            li += '5'
        elif rsp[i]=='2':
            li += '0'
        elif rsp[i]=='5':
            li += '2'

    return li