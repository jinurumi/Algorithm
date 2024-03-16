def solution(str_list):
    answer = []
    for i, d in enumerate(str_list):
        if d == "l":
            return str_list[:i]
        elif d =="r":
            return str_list[i+1:]
        else:
            pass
    return []