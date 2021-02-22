m,s=0,0
for i in range(1,10):
    t=int(input())
    if t>m:
        m=t
        s=i
print(m,s,sep='\n')