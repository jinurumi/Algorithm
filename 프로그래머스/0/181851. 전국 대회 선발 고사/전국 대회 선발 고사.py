def solution(rank, attendance):
    
    ans = []
    for i in range(len(rank)):
        if attendance[i]:
            ans.append(rank[i])
    
    ans= sorted(ans)
    print(ans)
    return rank.index(ans[0])*10000+rank.index(ans[1])*100+rank.index(ans[2])