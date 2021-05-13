from math import log

s = ['  *   ', ' * *  ', '***** ']

def star(shift):
    c = len(s)
    for i in range(c):
        s.append(s[i] + s[i])
        s[i] = "   " * shift + s[i] + "   " * shift
        
n = int(input())
k = int(log(n // 3, 2))
for i in range(k):
    star(int(pow(2, i)))
for i in range(n):
    print(s[i])