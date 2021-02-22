l=['-1']*(ord('z')-ord('a')+1)
s=input()
for i in range(len(s)-1,-1,-1):
    l[ord(s[i])-ord('a')] = str(i)
print(' '.join(l))