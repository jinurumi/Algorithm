def solution(array, n):
    ans = []
    array = sorted(array)
    ans = [ i-n for i in array]
    print(ans)
    aa = [abs(i) for i in ans]
    if n - min(aa) in array:
        return n - min(aa)
    else:
        return n + min(aa)
