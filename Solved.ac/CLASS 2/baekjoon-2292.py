def f(n):
    return 6*((n*n+n)/2+1)-5

p = int(input())

i = 1
li = [0]
while(True):
    li.append(f(i-1))
    if li[i-1] < p and p <= li[i]:
        print(i)
        break
    i += 1