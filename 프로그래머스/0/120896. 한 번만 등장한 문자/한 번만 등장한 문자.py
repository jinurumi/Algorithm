def solution(s):
    answer = ''
    ans=[0] * len(list(set(s)))
    s=list(s) # 문자열을 리스트로
    ss = sorted(list(set(s)))    # 총 등장하는 문자
    for i in range(len(s)):
        ans[ss.index(s[i])] += 1
    print(ss)
    print(ans)
    for i in range(len(ans)):
        if ans[i]==1:
            answer += ss[i]
    
    return ''.join(sorted(answer))