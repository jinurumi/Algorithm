def solution(left, right):
    answer = 0
    a=[]#left부터 right까지
    b=[]#약수의 개수
    for i in range(left, right+1):
        a.append(i)
    for i in range(len(a)):
        c=0
        for j in range(1, a[i]+1):
            if a[i]%j==0:
                c+=1
        b.append(c)
    d=0
    for i in range(len(a)):
        if b[i]%2==0:
            d+=a[i]
        else:
            d-=a[i]
    print(a)
    print(b)
    return d