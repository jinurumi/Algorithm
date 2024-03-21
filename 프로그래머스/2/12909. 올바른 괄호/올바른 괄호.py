def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] == "(": # "("가 나왔을때
            answer.append("(")
        else:   #"("가 나오지 않았을 때
            if len(answer)==0 or answer.pop()!="(": 
                return False
    
    if len(answer)==0:
        return True
    return False