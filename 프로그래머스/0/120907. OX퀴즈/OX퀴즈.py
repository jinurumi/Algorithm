def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        li = []
        li = quiz[i].split(" ")
        print(eval(''.join(li[:3])))
        if eval(''.join(li[:3])) == int(li[-1]):
            answer.append("O")
        else:
            answer.append("X")
        
    
    return answer