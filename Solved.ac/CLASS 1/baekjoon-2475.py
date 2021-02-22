l=list(map(int,input().split()))
s=0
for n in l:
    s+=n*n
print(s%10)