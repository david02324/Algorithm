import sys
input = sys.stdin.readline

for _ in range(int(input())):
    w = {}
    for _ in range(int(input())):
        inpt = input().split()
        if inpt[1] not in w.keys():
            w[inpt[1]] = 1
        w[inpt[1]] += 1
    
    a = 1
    for value in w.values():
        a *= value
    
    print(a-1)