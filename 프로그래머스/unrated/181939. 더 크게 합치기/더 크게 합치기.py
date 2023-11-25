def solution(a, b):
    c= int(str(a)+str(b))
    d=int(str(b)+str(a))
    if c>d:
        return c
    elif c<d:
        return d
    else:
        return c