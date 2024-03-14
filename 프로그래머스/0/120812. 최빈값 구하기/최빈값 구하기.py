def solution(array):
    answer = 0
    a =[]
    s = list(set(array))
    for idx, d in enumerate(s):
        a.append(array.count(d))
    print(s[a.index(max(a))])
    for i in a:
        if i == max(a):
            answer+=1
    if answer > 1:
        return -1
    
    return s[a.index(max(a))]