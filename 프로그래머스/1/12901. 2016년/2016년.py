def solution(a, b):
    days=0
    when = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(0,a):
        days+=day[i-1]
    
    days += b
    
    if days%7+1 ==7:
        return when[0]
    else:
        return when[days%7+1]