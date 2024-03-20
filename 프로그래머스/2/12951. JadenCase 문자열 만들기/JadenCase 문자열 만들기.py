def solution(s):
    answer = ''
    index=0
    for i in range(len(s)):
        if s[i]==" ":
            answer += " "
            index=0
        elif index==0:
            answer += s[i].upper()
            index+=1
        elif index!=0:
            answer += s[i].lower()
            index+=1
    return answer