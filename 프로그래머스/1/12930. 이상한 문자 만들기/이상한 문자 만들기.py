def solution(s):
    answer = ''
    index = 0
    for i in s:
        if i==" ":
            answer+=" "
            index = 0
        elif index%2== 0:
            answer+= i.upper()
            index+=1
        elif index%2==1:
            answer+= i.lower()
            index+=1
    return answer