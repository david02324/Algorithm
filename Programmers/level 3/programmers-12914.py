def factorial(n):
    val = 1
    for i in range(n,0,-1):
        val *= i
    return val

def combination(n,k):
    return factorial(n) // factorial(k) // factorial(n-k)

def solution(n):
    countTwo = n // 2
    countOne = n % 2
    count = 0
    
    while countTwo:
        count += combination(countTwo+countOne,countTwo)
        countTwo -= 1
        countOne += 2
        
    return (count + 1) % 1234567