def solution(num_list, n):
    ans = [num_list[i:i+n] for i in range(0,len(num_list) , n) ]
    print(len(num_list)//n)
    print(n)
    return ans