def solution(polynomial):
    answer = ''
    a,b= 0,0
    p = polynomial.split(" ")
    for i in range(len(p)):
        #print(p[i])
        if p[i].isdigit():
            #print(p[i],1)
            a +=int(p[i])
        elif p[i][-1]=='x':
            #print(p[i], 0)
            if p[i]=='x':
                #print(10)
                b+=1
            else:
                b += int(p[i][:-1])
    c=[]
    if b==1:
        c.append("x")
    
    elif b > 0:
        b = str(b)+"x"
        c.append(b)
    elif b==0:
        b = ''
    else:
        b = str(b)+"x"
        c.append(b)
    
    if a > 0:
        if len(c)==0:
            c.append(str(a))
        else:
            c.append("+")
            c.append(str(a))

    elif a==0:
        a = ''
    else:
        if len(c)==0:
            #c.append("-")
            c.append(str(a))
        else:    
            #c.append("-")
            c.append(str(a))
    print(c)
    return ' '.join(c)