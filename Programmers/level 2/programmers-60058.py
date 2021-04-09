def check_correct(s):
    status = 0
    
    for char in s:
        if char == '(':
            status += 1
        else:
            status -= 1
        
        if status < 0:
            return False
    
    return status == 0

def basket_reverse(s):
    new = ''
    for char in s:
        if char == '(':
            new += ')'
        else:
            new += '('
    
    return new

def solution(p):
    if p == '' or check_correct(p):
        return p
    
    status = 0
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            status -= 1
        elif p[i] == ')':
            status += 1
            
        if status == 0:
            u = p[:i+1]
            if len(p) > i+1:
                v = p[i+1:]
            break
        
    if check_correct(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + basket_reverse(u[1:-1])
            
    