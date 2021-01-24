import sys
input = sys.stdin.readline

# 모두 검사
def isPrimeNum(number):
    if number == 1:
        return 0
        
    for i in range(2,number):
        if number % i == 0:
            return 0
    
    return 1

# 소수의 성질 이용
def isPrimeNum(number):
    if number == 1:
        return 0
    
    primes = [2,3,5,7,11,13,17,19,23,29,31]
    for prime in primes:
        if number % prime == 0:
            if number == prime:
                return 1
            return 0
        
    return 1

# 입출력
n,numbers,count = input(),list(map(int,input().split())),0
for number in numbers:
    count += isPrimeNum(number)

print(count)