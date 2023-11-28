def solution(my_string):
    moum = 'aeiou'
    for st in my_string:
        if st in moum:
            my_string =my_string.replace(st,'')
            
        
        
    return my_string