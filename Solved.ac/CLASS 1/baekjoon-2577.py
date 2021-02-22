a,b,c=int(input()),int(input()),int(input())
k=str(a*b*c)
for i in range(10):
    print(k.count(str(i)))