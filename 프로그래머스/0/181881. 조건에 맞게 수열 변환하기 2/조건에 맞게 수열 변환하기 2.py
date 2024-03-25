import copy
def solution(arr):
    count = 0
    answer = []
    raw = arr
    while 1:
        raw = arr
        
        
        for i in range(len(arr)):
            if arr[i] >=50 and arr[i]%2==0:
                arr[i]=arr[i]//2
            elif arr[i]<=50 and arr[i]%2==1:
                arr[i]=arr[i]*2+1

        print(arr)
        count +=1
        # 이전 배열과 변환배열이 같다면
        a = 0
        print(arr)
        print(raw)
        for i in range(len(arr)):   
            if arr[i] == raw[i]:
                a +=1
        if len(arr)== a:

            return count # 변환횟수 return 

        print(count)
    
    
    
    
    
    
    
    
    
    
#     while 1:
        
#         arrr= copy.deepcopy(arr)
        
#         for i in range(len(arr)):
#             if arr[i] >= 50 and arr[i]%2==0:
#                 arr[i] = arr[i]//2
#             elif arr[i] < 50 and arr[i]%2==1:
#                 arr[i] = arr[i]*2 +1

#             count +=1
#         #print(arr)
        
#         for i in range(len(arr)):
#             if arr[i]==arrr[i]:
#                 answer.append(1)
#         if sum(answer) == len(arr):
#             return count
                
        
        
        
