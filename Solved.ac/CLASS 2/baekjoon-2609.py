def gcd(x,y):
    while y:
        x,y = y, x%y
    return x
n,m = map(int,input().split())
print(gcd(n,m))
print(n * m // gcd(n,m))