def solution(n):
    a = []
    for i in range(1,11):
        ans=1
        for j in range(1,i+1):
            ans*=j
        a.append(ans)
    for i in range(len(a)):
        if a[i]>n:
            return i
        elif a[i]==n:
            return i+1