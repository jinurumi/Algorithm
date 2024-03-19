def gcd(a,b):
    if a % b == 0:
        return b
    else:
        print(a,b)
        return gcd(b, a%b)
    
    
def solution(n, m):
    answer = []
    b = gcd(n,m)
    print(b)
    a = abs(n*m) / b
    return [b,a]