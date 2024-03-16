def solution(my_string, queries):
    answer = ''
    my_string = list(my_string)
    for i in range(len(queries)):
        a = my_string[queries[i][0] : queries[i][1]+1]
        my_string = my_string[:queries[i][0]]+ a[::-1] + my_string[queries[i][1]+1:]        
    return ''.join(my_string)