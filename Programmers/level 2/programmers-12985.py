def solution(n,a,b):
    round = 1
    while True:
        x = max(a,b)
        n = min(a,b)
        
        if x%2 == 0 and x - 1 == n:
            return round
        
        a += 1
        b += 1
        a //= 2
        b //= 2
        
        round += 1