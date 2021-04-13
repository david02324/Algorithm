from itertools import permutations

def tuple_to_int(tuple):
    return int(''.join(tuple))

def is_prime(n):
    if n == 0 or n == 1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if not n % i: return False
    return True

def solution(numbers):
    count = 0
    numbers_set = set()
    for i in range(1,len(numbers)+1):
        numbers_set |= set(map(tuple_to_int,permutations(numbers,i)))
    
    for number in list(numbers_set):
        if is_prime(number):
            count += 1

    return count