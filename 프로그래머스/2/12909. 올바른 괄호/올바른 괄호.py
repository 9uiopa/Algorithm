def solution(s):
    if s.startswith(')'):
        return False

    l = list(s)
    stk = []
    for i,x in enumerate(s):
        if x == ')' :
            if len(stk)>0 :
                stk.pop()
            else :
                return False
        else :
            stk.append(x)
    if len(stk)>0:
        return False
    
    return True
