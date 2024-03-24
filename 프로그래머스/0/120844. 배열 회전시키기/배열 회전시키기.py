def solution(numbers, direction):
    answer = []
    if direction=='right':
        ans = [numbers[-1]]
        for i in range(0,len(numbers)-1):
            ans.append(numbers[i])

    else:
        ans = numbers[1:]
        ans.append(numbers[0])
    return ans
    
 
