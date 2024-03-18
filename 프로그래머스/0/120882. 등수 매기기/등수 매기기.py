def solution(score):
    answer = [] # 평균점수
    rank = [] # 순위
    ans = []   # 최종 답
    for s in range(len(score)):
        answer.append((score[s][0]+score[s][1])/2)
    print(answer)
    rank = sorted(answer, reverse=True)
    print(rank)
    for i in range(len(score)):
        ans.append(rank.index(answer[i])+1)
    return ans
