def solution(numlist, n):
    answer = []
    for i in range(len(numlist)):
        answer.append([abs( numlist[i]-n), numlist[i]])
    
    a=sorted(answer,key = lambda x : [x[0], -x[1]])
    return [ i[1] for i in a]