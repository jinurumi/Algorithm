def solution(price, money, count):
    for c in range(1,count+1):
        money -= c * price
        
    if money>=0:
        return 0
    elif money<0:
        return abs(money)
        
    