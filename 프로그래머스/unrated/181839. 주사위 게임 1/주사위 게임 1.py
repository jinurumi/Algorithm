def solution(a, b):
    score = 0
    if (a+b)%2==1:
        return 2*(a+b)
    elif a%2==1 and b%2==1:
        return a*a+b*b
    else:
        return abs(a-b)