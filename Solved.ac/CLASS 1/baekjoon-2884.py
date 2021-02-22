h,m = map(int,input().split())
if m-45 < 0:
    if h-1 < 0:
        h = 24
    h -= 1
    m += 60
m -= 45
print(h,m)