from collections import Counter
l=Counter(input().upper()).most_common(2)
print(l[0][0] if len(l)==1 or l[0][1]!=l[1][1] else '?')