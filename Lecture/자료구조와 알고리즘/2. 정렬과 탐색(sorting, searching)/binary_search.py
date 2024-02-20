def solution(L, x):
    lower = 0
    upper = len(L)-1
    
        while lower <= upper :
            middle = (lower+upper) // 2
            if L[middle] == x :
                return middle
                quit()
            #elif L[lower] == x :
            #    return lower
            #    quit()
            #elif L[upper] == x :
            #    return upper
            #    quit()
            elif L[middle] < x :
                lower = middle+1
                continue            
            else:
                upper = middle -1
                continue 
    else :
        answer = -1
    return answer