def gcd(a, b):
    if a % b ==0:
        return b
    elif b == 0 :
        return a
    else:
        return gcd(b, a%b)
    
def solution(arr):
    a = arr[0]
    for i in range(1,len(arr)):
        a = a * arr[i] // gcd(arr[i],a)

    return a