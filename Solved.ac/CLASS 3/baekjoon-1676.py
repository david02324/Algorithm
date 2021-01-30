# 1
def zeroCount(n):
    f = 0
    t = 0
    for i in range(n,0,-1):
        k = i
        while k % 5 == 0 or k % 2 == 0:
            if k % 5 == 0:
                k //= 5
                f += 1
            if k % 2 == 0:
                k //= 2
                t += 1
    
    return min(f,t)

print(zeroCount(int(input())))

# 2
n = int(input())
print(n // 5 + n // 25 + n // 125)