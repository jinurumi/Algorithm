def solution(arr, queries):
    answer =[]
    for i in range(len(queries)):
        ans =[]
        for j in range(queries[i][0],queries[i][1]+1):
            if arr[j] > queries[i][2]:
                ans.append(arr[j])
        if len(ans)>0:
            answer.append(min(ans))   
        else: 
            answer.append(-1)
    return answer