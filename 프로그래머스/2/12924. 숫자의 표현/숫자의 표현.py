def solution(n):
    count = 0
    a=1
    while a <= n:
        answer = 0
        for i in range(a,10001):
            answer+= i
        

            if answer == n:
                count +=1
                break
            if answer > n:
                break
        a +=1
    return count