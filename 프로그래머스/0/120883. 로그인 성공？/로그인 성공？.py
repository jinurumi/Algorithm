def solution(id_pw, db):
    a=[]
    for i in db:
        if i[0]==id_pw[0] and i[1]==id_pw[1]:
            return "login"
        elif i[0]==id_pw[0] and i[1]!=id_pw[1]:
            a.append("wrong pw")
        
    if "wrong pw" in a:
        return "wrong pw"
    else:
        return "fail"
    