# 그냥 나눠보는 방법(느림)
m, n = map(int,input().split())

def isPrime(number,primes):
    sqrt = int(number**0.5)
    for prime in primes:
        if prime <= sqrt:
            if i % prime == 0:
                return False
        else:
            return True

primes = [2]
for i in range(3,n+1):
    if isPrime(i,primes):
        primes.append(i)

print('\n'.join([str(i) for i in primes if m <= i]))

# 에라토스테네스의 체
m, n = map(int,input().split())

def isprime(m, n):
    primes = [False,False] + [True] * (n - 1)
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*2, n+1, i):
                primes[j] = False

    for i in range(m,n+1):
        if primes[i]:
            print(i)

isprime(m,n)