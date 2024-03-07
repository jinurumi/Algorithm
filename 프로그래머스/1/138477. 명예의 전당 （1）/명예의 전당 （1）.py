def solution(k, score):
    answer = []
    ans = [] # 그날 명예 리스트
    for i in range(0,len(score)):
        answer.append(sorted(score[:i+1],reverse=True))
        
    for i in range(0,len(answer)):
        if len(answer[i]) <= k:

            answer[i] = answer[i][:i+1]
            ans.append(answer[i][-1])
        else:
            ans.append(answer[i][k-1])

    
    return ans