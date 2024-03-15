def solution(a, b, c, d):
    ss=[0]*len(set([a,b,c,d]))
    s = list(set([a,b,c,d]))
    
    for i in [a,b,c,d]:
        if i in s:
            ss[s.index(i)]+= 1
    
    if len(s) == 1 :
        return 1111*s[0]
    elif len(s) == 2 :
        if ss[0]==2:
            return (s[0]+s[1]) * abs(s[0]-s[1])
        elif ss[0]==3 or ss[1]==3:
            return (10* s[ss.index(3)] + s[ss.index(1)])**2
    elif len(s) ==3:
        ans =1
        for i in range(len(ss)):
            if ss[i]==1:
                ans *=s[i]
        return ans
    else:
        return min(s)
    