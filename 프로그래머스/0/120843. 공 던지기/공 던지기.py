def solution(numbers, k):
    count = 0
    if len(numbers) < k*2-1:
        numbers = numbers * (((k*2-1)//len(numbers))+1)
        
    for i in range(1, len(numbers)+1,2):
        count+=1
        if count == k:
            return numbers[i-1]
    