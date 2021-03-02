def power(r):
    if not r:
        return 1
    elif r == 1:
        return a % c
    if r % 2:
        return power(r // 2)**2 * a % c
    else:
        return power(r // 2)**2 % c
a,b,c = map(int,input().split())
print(power(b))