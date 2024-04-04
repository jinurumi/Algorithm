def solution(citations):
    a=[]
    for i in range(0,1001):
        b = []
        for j in citations:
            if i <= j:
                b.append(j)
        if len(b)>=i:
            a.append(i)
    return sorted(a)[-1]